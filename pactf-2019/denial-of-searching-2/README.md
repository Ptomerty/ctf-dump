# Denial of Searching 2

We're given a `quickhash()` function and told that someone is "DoSing" the server through abuse of a hashtable. Most likely, someone is abusing the weakness of the custom hash function and creating many collisions, wreaking havoc on the hashtable.

I wrote a script to iterate through all of the provided "posts" and count the number of collisions of each user, then printed out the highest collision count at 1023 collisions. 

Note: removed `logs/` folder for space reasons (89 MB, yikes). Hash: `7afeeb1b19f0e2e3b0699deacd9d603dfa4139a2a57e9156933b874260f14ea8  serverlog.4af8e4389eff.7z`

### Flag: `flag{Dos_Funded_Actors}`