# Hack The Box Hack the Boo 2024 CTF

My second CTF! I was able to build upon what I learned from Cyber Apocalypse, which enabled me to earn more flags in a limited timeframe.
I also learned new things, like this was my first time using pwntools! Even if it was only to pack an integer into a byte string 😂

This time around, most of the challenges I completed were easily solved in the browser or with a quick objdump, and I would try to move quickly to the next. So there's not as much documentation, but I would like to share some context here for my two favorites from this event: hybrid unifier and El Mundo!
- For hybrid unifier, I was able to use the provided code to determine how the application worked and then build my own "session" class that has exactly what I needed to decrypt and encrypt the various information. The most important piece to this puzzle is the math used to calculate the session key. By providing the number 0 for the client public key, I could guarantee the session key value.
- For El Mundo, there was some provided code that utilizes pwntools, which I'm unfamiliar with.
Instead of losing time in the competition, I elected to simply write my own solution in the same fashion as other examples of mine,
using the socket module. However, when it came to packing the necessary address, the to_bytes() function didn't cut it.
So I went ahead and used pwntools for that.

I earned 6/12 flags for the following challenges:

Pwn:
- El Pipo
- El Mundo

Crypto:
- hybrid unifier

Reversing:
- LinkHands

Coding:
- Replacement
- MiniMax