#!/usr/bin/python
BASE = 2

def translate(str):
	ar = str.split(" ")
	ar0 = bin(int(ar[0], 8))[2:].zfill(15)
	ar1 = bin(int(ar[1], 8))[2:].zfill(15)
	mantissa0 = ar0[1:]
	mantissa1 = ar1[1:]
	total = 0

	subtotal = 0
	for i in range(14):
		subtotal += int(mantissa0[i], 10) * (BASE**(-1 * (i + 1)))
	if ar0[0] == '1':
		subtotal *= -1
	total += subtotal
	print('mantissa 0: ', subtotal)

	subtotal = 0
	for i in range(14):
		subtotal += int(mantissa1[i], 10) * (BASE**(-1 * (i + 15)))
	if ar0[0] == '1':
		subtotal *= -1
	total += subtotal
	print('mantissa 1: ', subtotal)

	return total

inp = input("Enter octal: ")
output = translate(inp) / 2**-4
print(str(output)[:10]) # truncate to double precision