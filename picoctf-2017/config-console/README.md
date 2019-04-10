# Config Console

quick explanation: we no longer have a give_flag function. 
1. First, we overwrite exit() to loop() so that we have infinite format string attacks. one thing to note is that since this is 64-bit, there are a million nul bytes after the addresses: therefore, we add some padding, move to the *next* space on the stack, then put *format specifier first*.
2. We then grab a random libc address from the stack. Using offline GDB, we get the absolute offsets between strlen, system, and our leak.
3. We populate strlen by calling login() so that strlen@plt no longer points in 0x400000, but has been populated with the correct libc address.
4. Overwrite the strlen@plt with system@plt, 4 bytes at a time.  python formatting is confusing but this works
5. Call "p sh" and the binary will run system("sh"). We've got shell!

A few things learned:
* Format specifier trick. When given an address like \x11\x11\x60\x00, the null byte will prevent printf from reading a format specifier. Therefore, to combat this, we can do "%17$lx" + ADDRESS so that the format string will read *after* itself.
* Python formatting is weird.
* Python will buffer output on pause(), so it seemed like my overwrite wasn't working for a good hour and a half.
* It's easier to grab libc from the shell server then use LD_PRELOAD to ensure you have correct offsets in libc from the get-go. (Thanks r3ndom)