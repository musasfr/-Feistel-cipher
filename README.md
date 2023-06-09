# Feistel-cipher

Key Generation, Encryption, and Decryption in Python
Encryption and Decryption Script (For Encryption.py)

This script implements a custom encryption and decryption algorithm using Python.
The script defines three functions: generate_keys, encrypt, and decrypt.

## How it works

The generate_keys function takes in three arguments:
K, H, and P. 
K is the key used to generate the subkeys, 
H is a user-defined permutation,
and P is a fixed permutation defined in the function.
The function applies the permutation H to the key K and generates two subkeys k1 and k2 using bitwise operations.

The encrypt function takes in four arguments: 
N, k1, k2, and pi.
N is the message to be encrypted,
k1 and k2 are the subkeys generated by the generate_keys function, and pi is a user-defined shift order.
The function applies the shift order pi to the message N, splits it into two halves, and performs several rounds of bitwise operations using the subkeys and a fixed permutation to generate the encrypted message.

The decrypt function takes in four arguments:
C, k1, k2, and pi.
C is the encrypted message,
k1 and k2 are the subkeys generated by the generate_keys function, 
and pi is the same shift order used in the encryption process.
The function applies the shift order to the encrypted message, splits it into two halves, and performs several rounds of bitwise operations using the subkeys and the inverse of the fixed permutation used in the encryption process to recover the original message.

## How to execute

To execute this script, you need to have Python installed on your computer.
Open a terminal or command prompt, navigate to the directory where you saved this script, and run it using the command:

python Encryption.py

The script will prompt you to enter values for several variables:

K: The key used to generate the subkeys.
Enter 8 integers separated by spaces.

H: The user-defined permutation used in key generation.
Enter 8 integers separated by spaces.

pi: The user-defined shift order used in encryption/decryption. 
Enter 8 integers separated by spaces.

N: The message to be encrypted.
Enter 8 integers separated by spaces.

After entering these values, press Enter to run the script. 
The script will generate two subkeys using the provided key and permutation, encrypt the message using these subkeys and shift order, print out both subkeys and encrypted message then decrypt it again using these same subkeys and shift order then print out decrypted message.



## Example Here is an example of how this script can be used:

``` python Encryption.py
Please enter the values of K: (K is the key used to generate the subkeys) separated by spaces: 1 2 3 4 5 6 7 8 
Please enter the values of H: (H is the user-defined permutation used) separated by spaces: 7 6 5 4 3 2 1 0 
Please enter the values of pi: (pi is the user-defined shift order used) separated by spaces: 0 1 2 3 4 5 6 7
Please enter the values of N: (N is the message to be encrypted) separated by spaces: 1 2 3 4 5 6 7 8
Subkeys: [6, 7, 4, 5] [0, 0, 0, 0]
Encrypted message: [4, 5, 6, 7, 4, 5, 6, 7]
Decrypted message: [1, 2, 3, 4, 5, 6, 7, 8]
In this example, the user entered 1, 2, 3, 4, 5, 6, 7, 
and 8 as the key K, 7, 6, 5, 4, 3, 2, 1, 
and 0 as the permutation H, 0, 1, 2, 3, 4, 5, 6, 
and 7 as the shift order pi, and 1, 2, 3, 4, 5, 6, 7,
and 8 as the message to be encrypted.
The script generated two subkeys [6,7,4,5] and [0,0,0,0] using these values and encrypted the message to get [4,5,6,7,4,5,6,7].
then decrypted this encrypted message to recover the original message [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8].
