# Flagsay-2

Our input's not even on the buffer anymore! The solution is to overwrite stack addresses that point to stack addresses. For example, 0xffffaaaa -> 0xffffbbbb (location) which has a value of 0.
0. Leak libc and calculate offset: standard stuff.
1. Break right before the vulnerable printf and examine the stack. Look for addresses that point to another location on the stack that then point to empty spots. For example, %9$p points to %16$p in memory, which has a value of 0.
2. Write the full (!) address to the two registers, aka 0x08049970 bytes of data. This will take a while.
    2a. Since we're writing the same thing + 2 to the second register, we can take advantage of the bytes already written and just add an "AA" as a spacer for %n.
3. Overwrite the second addresses with the leaked system address.
4. Escape the slashes with "; sh ;"
5. You've got shell!

A few things learned:
* IF YOU DO NOT RECV() THE INPUT, YOU WILL DROP INTO INTERACTIVE() BEFORE THE FMT STR IS SENT. This will break your exploit!
* If you can't preload libc (like I couldn't), hop onto the webshell and calculate libc offsets / stack offsets there before writing your exploit.
* Cool recv() and python stuff.