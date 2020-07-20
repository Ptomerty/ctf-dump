#!/usr/bin/python3

import re
import zipfile
import io

with open("flag.zip", "rb") as f:
	file_bytes = f.read()

header = 0x26
footer = 108

while True:
	try:
		for i in range(100):
			last = len(re.findall(r"PK\x03\x04\x14\x00", file_bytes)) - 1
			if last > 2:
				# if there are more than 2 header matches, it's most likely STORE
				# snip STORE zips
				file_bytes = file_bytes[last*header : -1*last*footer]

			# decompress remaining ZIP file
			zfile = zipfile.ZipFile(io.BytesIO(file_bytes), "r")
			file_bytes = zfile.read(zfile.infolist()[0])
		with open("intermediary.zip", "wb") as f:
			print("saving intermediary output to check")
			f.write(file_bytes)
	except KeyboardInterrupt:
		exit()
	except:
		print(file_bytes)
		exit()
