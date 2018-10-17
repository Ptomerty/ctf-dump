# Format

The way you were *supposed* to do this was by exploiting `printf(buff);` in line 17, resulting in a Format String Attack. You could leak values from the stack using this, and eventually get the flag.

However, I took a different approach. I noticed that `srand(time(0));` allowed for improper seeding of rand(). I then took tips from another CTF challenge and created a simple `guess.c` which would initialize the same random seed. Finally, I ran `~/guess && ./format` to get the correct flag.