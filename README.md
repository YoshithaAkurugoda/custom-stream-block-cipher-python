# Custom Stream Cipher and Block Cipher Implementation (Python)

This project implements two educational cryptographic systems developed as part of a cybersecurity portfolio assignment.

The goal was to explore how encryption algorithms work internally by building simplified versions of both a **stream cipher** and a **block cipher with GCM mode**.


## Project Components

### 1. Stream Cipher using LCG PRNG

This implementation creates a stream cipher using a **Linear Congruential Generator (LCG)** as a pseudo-random keystream generator.

Encryption is performed using XOR between plaintext characters and the generated keystream.

Features:

- Custom LCG pseudo-random number generator
- XOR based encryption and decryption
- Character-by-character keystream generation
- Detailed encryption breakdown for the first 9 characters

The program demonstrates how stream ciphers generate keystream values and combine them with plaintext.


### 2. Custom Block Cipher with GCM Mode

The second implementation builds a simplified **Substitution-Permutation Network (SPN)** block cipher.

Key properties:

- Block size: 9 bytes (72 bits)
- Key size: 9 characters
- 4 rounds of substitution and permutation
- Final key mixing round

The cipher is then used in a simplified **GCM-style mode** that includes:

- Counter mode encryption
- A simplified GHASH-style authentication tag

This demonstrates the principles behind authenticated encryption.


## Technologies Used

- Python
- Cryptography concepts
- Stream cipher design
- Block cipher design
- XOR operations
- Counter mode encryption
- Authentication tagging


## How to Run

### Stream Cipher


python stream_cipher.py


Enter an integer key when prompted.

The program will:

1. Display encryption details for the first characters
2. Encrypt the message
3. Display ciphertext
4. Decrypt the ciphertext back to the original message


### Block Cipher with GCM Mode


python block_cipher_gcm.py


Enter a **9 character key** when prompted.

The program will:

1. Encrypt the message
2. Output ciphertext
3. Generate an authentication tag


## Example Message Used


Convert $502.89 AUD to 98283.04 LKR on 5 January 2026.

## Learning Outcomes

This project helped develop practical understanding of:

- Stream cipher keystream generation
- XOR based encryption
- Block cipher round structures
- Substitution and permutation layers
- Counter mode encryption
- Authentication tags in modern cryptography

Building simplified cryptographic systems from scratch provides insight into how modern encryption algorithms function internally.

## Author

Yoshitha Akurugoda  
Cybersecurity Undergraduate
