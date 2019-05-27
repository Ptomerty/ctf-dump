# Can You See the Future?

This is a good problem. We're given an RNG, and a hint that this RNG is used in Java. The problem lies in the fact that Java uses an incredibly insecure [LCG](https://en.wikipedia.org/wiki/Linear_congruential_generator), which can be easily cracked. For further reading, see [this article](https://jazzy.id.au/2010/09/20/cracking_random_number_generators_part_1.html).

I wrote a quick reverse() function that undoes the mangling done by gen_random_int() and reversed the two primes from `key2.pem`. Since we only need two outputs to completely crack an LCG, I fed these two numbers into Jazzy's provided script and got a seed of `105847457969211`.

Going back to the provided script, I initialized the RNG to said seed and checked the next 3 generated primes to ensure that they were close enough to the original primes and that I had the correct seed. I then continued the RNG, generated another key, and deciphered the message.

### Flag: `flag{this_is_the_rng's_power}`