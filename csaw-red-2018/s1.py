import string
from Crypto.Cipher import DES

def is_printable(s):
    return all(c in (string.printable) for c in s)

def get_blocks(data, block_size):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

c = open("destiny.enc", "rb").read()
IV = '66642069'
bs = DES.block_size

assert (len(c) % bs == 0), "[-] Ciphertext not a multiple of DES blocksize"

blocks = get_blocks(c, bs)

for b in blocks:
    x = xor_strings(b, IV)
    if (is_printable(x)):
        print x


#On be   
#half of 
#the Admi
#ssions C
#ommittee
#my pleas
#ure to o
#ffer you

#Admissio
#ns Commi
#ttee

for j in range(10):
	p = "ssions C"
	k = xor_strings(blocks[j], p)

	s = ""
	for i in xrange(len(blocks)):
	    if (i % 2 == 0):
	        b = xor_strings(blocks[i], IV)
	    else:
	        b = xor_strings(blocks[i], k)

	    s += b

	if 'flag' in s:
		print s
