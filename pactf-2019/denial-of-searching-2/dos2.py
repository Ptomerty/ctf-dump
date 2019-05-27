#!/usr/bin/env python2

import os
import codecs
import binascii

def quickhash(str):
	hash_ = 0
	for i, char in enumerate(str):
		# print("char is", ord(char))
		hash_ += 31 ** i * ord(char)
		hash_ = hash_ % (2**32)
	return hash_

def num_collisions(path):
	with open("logs/" + path, 'rb') as f:
		# print("Name is", path)
		content = f.read().splitlines()
		content = list(filter(None, content))
		# print content
		hashes = []
		for line in content:
			hashes.append(quickhash(line))
		# print hashes
		collisions = len(hashes) - len(set(hashes))
		return (collisions, path)
		# print path + " has " + str(collisions) + " collisions."

coll = []

for path in os.listdir("logs/"):
	# print "Current path: " + path
	coll.append(num_collisions(path))
print sorted(coll, reverse=True)[0][1]
