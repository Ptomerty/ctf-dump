# We're in the Endgame Now

I made this challenge a lot harder than it had to be. You simply had to reconstruct a PNG, adding back in the IPNG chunk `89 50 4E 47 0D 0A 1A 0A `, part of the IHDR chunk `00 00 00 0D 49 48 44 52 00000284 00000176 08060000 00F70589 C0000018`, and adding in the provided ending data and an IEND chunk in order to get the fixed image.

### Flag: `flag{i_am_ironman_3000}`