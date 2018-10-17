#!/usr/bin/env python

from subprocess import *
import string

input = 'B'
for input in string.printable:
	out = check_output(["./hgp", input + 'yummy_h45h_br0wn'])
	if out == '22c15d5f23238a8fff8d299f8e5a1c62\n':
		print input