#!/usr/bin/env python

from pwn import *
import string

r = process("./quackmeup")

# print r.recvline()

test = string.letters + string.digits + '{}_'
# print test

r.sendline(test)

# r.recvline()

# r.recvuntil("ciphertext:")
r.recvuntil("text:")

key_list = r.recvuntil("Now").split("Now")[0].strip().split(" ")
test_list = list(test)

assert (len(test_list) == len(key_list))

r.recvuntil(":")
cipher_list = r.recvuntil("T").split("T")[0].strip().split(" ")
print cipher_list

out = ''
for l in cipher_list:
	out += test_list[key_list.index(l)] 

print out
