# Final Rho

Taking a hint from the problem, we are led towards [Pollard's Rho Algorithm](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm), which allows us to quickly factorize most integers. 

Using Pollard's rho, we are able to factorize N into its two factors p and q. From there, we can quickly calculate phi = (p-1)(q-1), find the private key d = e^1 mod phi, and decrypt the cipher.