# Feistel-cipher
Key Generation, Encryption, and Decryption in Python
This repository contains a Python implementation of key generation, encryption, and decryption algorithms.

Usage
The code defines three functions: generate_keys, encrypt, and decrypt.

The generate_keys function takes as input a key K of length 8 and returns two subkeys k1 and k2 of length 4. For example:

K = [0, 0 ,0 ,0 ,0 ,0 ,0 ,1]
k1,k2=generate_keys(K)
The encrypt function takes as input a block N of length 8 and the two subkeys k1 and k2, and returns the encrypted text C of length 8. For example:

N = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1]
C=encrypt(N,k1,k2)
The decrypt function takes as input a block C of length 8 and the two subkeys k1 and k2, and returns the decrypted text N of length 8. For example:

N=decrypt(C,k1,k2)
Example
Here is an example that demonstrates how to use the functions to encrypt and decrypt a message:

K = [0, 0 ,0 ,0 ,0 ,0 ,0 ,1]
N = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,1]

k1,k2=generate_keys(K)
C=encrypt(N,k1,k2)
N=decrypt(C,k1,k2)
This code generates the subkeys from the key K, encrypts the message N using the subkeys to produce the ciphertext C, and then decrypts the ciphertext using the subkeys to recover the original message.
