#!/usr/bin/python3

import sys

def sign_extend(value,bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

def reverse(input):

	opname_arr = ["MNZ","MLZ","ADD","SUB","AND","OR","XOR","ANT","SL","SRL","SRA"]

	cmode = int(input[0:2], 2)
	carg = int(input[2:18], 2)
	bmode = int(input[18:20], 2)
	barg = int(input[20:36], 2)
	amode = int(input[36:38], 2)
	aarg = int(input[38:54], 2)
	opcode = int(input[54:], 2)

	carg = str(sign_extend(carg, 16))
	barg = str(sign_extend(barg, 16))
	aarg = str(sign_extend(aarg, 16))

	if cmode != 0:
		cmode = chr(cmode + 64)
	else:
		cmode = ''

	if bmode != 0:
		bmode = chr(bmode + 64)
	else:
		bmode = ''
	if amode != 0:
		amode = chr(amode + 64)
	else:
		amode = ''

	op = opname_arr[opcode]
	return '{0} {1}{2}, {3}{4}, {5}{6}'.format(op, amode, aarg, bmode, barg, cmode, carg)

def main():
	if len(sys.argv) == 1:
		print('Too few arguments: pass file as second argument.')
		exit(1)

	filename = sys.argv[1]
	counter = 0
	with open(filename) as f:
		code_rev = f.readlines()
		if len(sys.argv) == 3 and sys.argv[2] == 'reverse':
			code_rev = reversed(code_rev)
		for line in code_rev:
			print("#{0}. {1}".format(counter, reverse(line)))
			counter += 1

main()