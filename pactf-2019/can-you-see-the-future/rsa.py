#!/usr/bin/env python3 

from Crypto.PublicKey import RSA  # stands for Reyn-Shulk Algorithm
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import isPrime, inverse, GCD
import codecs
# from secret import secret_seed, flag

decode_hex = codecs.getdecoder("hex_codec")

N_BITS = 512
a = 2**511
b = 2**512

# very secure: used in Java in billions of devices!
class RNG:
    """This is a linear congruential pseudorandom number generator, as defined by D. H. Lehmer and
    described by Donald E. Knuth in The Art of Computer Programming, Volume 3: Seminumerical
    Algorithms, section 3.2.1."""
    def __init__(self, seed):
        """Given a seed value, initializes the RNG."""
        # self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)
        self.seed = seed

    def next(self, bits=32):
        """Updates the state and returns the given number of random bits as an integer. Must be less than
        48."""
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return self.seed >> (48 - bits)

    
def lcm(a, b):
    return a * b // GCD(a, b)

def gen_random_int(a, b, rng):
    """Gets a random integer in the interval [a, b)."""
    x = rng.next(32)
    #print(x)
    return int(a + (x / (2 ** 32)) * (b - a))

def gen(x):
    return int(a + (x / (2 ** 32)) * (b - a))

def reverse(val):
    val -= a
    val /= (b-a)
    val *= 2**32
    return int(val)

def gen_random_prime(rng):
    # select an odd 1024-bit number at random using random.random()
    num = gen_random_int(2 ** (N_BITS - 1), 2 ** N_BITS, rng)
    # decrement until prime
    while not isPrime(num):
        num -= 1
        # prevent underflow
        if num == 2 ** (N_BITS - 1):
            num = 2 ** N_BITS - 1
    return num

def gen_random_key(rng):
    # generate p and q at random
    p = gen_random_prime(rng)
    q = gen_random_prime(rng)
    n = p * q
    e = 65537  # standard default
    # compute d, the inverse of e mod lcm(p - 1, q - 1)
    d = inverse(e, lcm(p - 1, q - 1))
    return RSA.construct((n, e, d, p, q))

def encrypt(data, key):
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(data)

def decrypt(data, key):
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(data)

p1 = 0xb02244107fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdf
p2 = 0xa2dde4227fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff25
p3 = 0xdb4167e27fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff17
p4 = 0xea80d64d7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc7

rng = RNG(105847457969211)

print(reverse(p1))
print(reverse(p2))

assert gen_random_prime(rng) == p2, "Prime 2 failed!"
print("Prime 2 matches!")
assert gen_random_prime(rng) == p3, "Prime 3 failed!"
print("Prime 3 matches!")
assert gen_random_prime(rng) == p4, "Prime 4 failed!"
print("Prime 4 matches!")

key4 = gen_random_key(rng)
with open('data/message', 'rb') as f:
    content = f.read()
    content = decode_hex(content)[0]
    # print(content)
    print(decrypt(content, key4))
