# Not OTP

This one gave people a lot of trouble, probably because they didn't guess very well :shrug:

We're given two strings encoded with a one-time pad. This means that both strings are vulnerable to crib dragging. I utilized [this tool](https://github.com/SpiderLabs/cribdrag) to assist me.

One guess made was `easyctf{` (we can tell this is part of the flag), which allowed the first half of the string to be decrypted. However, nothing after was showing up. This is when I made the hunch that 1337 text would be used in the flag. Trying `dr4g` as an input, we are greeted with `stem` in the output. 

Elaborating on this leads to `cr1b_dr4g`, which expands to `cryptosystems`, which fills in with `crack`.

FLAG: easyctf{otp_ttp_cr1b_dr4gz}
