from pwn import *



def solve():
	def parse(str):
		split = str.split('\n')[0].split(' ')
		# print split
		src = int(split[3][1:-1])
		dest = int(split[0][2:])
		# print src, dest
		num = False
		operand = 0
		if split[4][0] == '%':
			operand = int(split[4][1:])
		else:
			operand = int(split[4][0])
			num = True
		# print num, operand
		operation = split[2]
		# print operation
		if operation == 'add':
			if num:
				array[dest] = array[src] + operand
			else:
				array[dest] = array[src] + array[operand]
		elif operation == 'sub':
			if num:
				array[dest] = array[src] - operand
			else:
				array[dest] = array[src] - array[operand]
		elif operation == 'mult':
			if num:
				array[dest] = array[src] * operand
			else:
				array[dest] = array[src] * array[operand]
		elif operation == 'xor':
			if num:
				array[dest] = array[src] ^ operand
			else:
				array[dest] = array[src] ^ array[operand]
		elif operation == 'or':
			if num:
				array[dest] = array[src] | operand
			else:
				array[dest] = array[src] | array[operand]
		elif operation == 'and':
			if num:
				array[dest] = array[src] & operand
			else:
				array[dest] = array[src] & array[operand]


	array = [0 for i in range(40)]
	# print array

	input1 = r.recvline().split('\n')[0]
	# print input1
	array[0] = int(input1.split(' ')[2], 16)

	a = r.recvline()
	while a.split(' ')[0] != '>show':
		parse(a)
		# print array
		a = r.recvline()


	list = a.split(' ')
	# print list
	total = 0
	total += array[int(list[1][1:])]
	total += array[int(list[3][1:])]
	total += array[int(list[5][1:])]
	total += array[int(list[7][1:])]
	total += array[int(list[9][1:])]
	total += array[int(list[11][1:])]
	total += array[int(list[13][1:])]

	# print total

	r.sendline(str(total))

r = remote('misc.chal.csaw.io', 10101)

r.recvuntil('***************************************************************************\n')

for i in range(100):
	r.recvuntil('***************************************************************************\n')
	solve()

r.interactive()