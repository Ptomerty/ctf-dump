from Crypto.Cipher import DES
import binascii

key = str(0x0101010101010101)
iv = '66642069'
cipher = DES.new(key, DES.MODE_OFB, iv)
c =  open('destiny.enc', 'r').read()
print cipher.decrypt(plaintext)
