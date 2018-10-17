#!/usr/bin/env python

from pwn import *
import time

pico = 0

if pico:
    r = remote('2018shell2.picoctf.com', 9850)
else:
    #env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico64.libc.so.6")}
    # env = {"LD_LIBRARY_PATH": "."}
    r = process("./contacts_orig")
    gdb.attach(r)


libc = ELF('./pico64.libc.so.6')

r.interactive()