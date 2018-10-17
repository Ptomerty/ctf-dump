# Soupstitution Cipher

The trick here (after unobfuscating) is that python's isDigit() also accepts characters like ` 	෯ ` as legitimate numbers. I therefore calculated BY HAND the various numbers you'd need to match a hex-encoded 's0up', starting from hex * 10^n and subtracting all the way down, eventually netting me a valid answer.

FLAG: ߉༩෯۹୯໕1