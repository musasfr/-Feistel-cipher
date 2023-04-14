# Define a function to generate the subkeys
def generate_keys(K, H, P):
    # Apply the user-defined permutation H to the key K
    K = [K[H[i]] for i in range(8)]
    # Generate the first subkey k1 by XORing pairs of elements from K
    k1 = [K[i] ^ K[i + 4] for i in range(4)]
    # Generate the second subkey k2 by ANDing pairs of elements from K
    k2 = [K[i + 4] & K[i] for i in range(4)]
    # Rotate k1 to the left by two positions
    k1 = k1[2:] + k1[:2]
    # Rotate k2 to the right by one position
    k2 = [k2[-1]] + k2[:-1]
    # Return the two subkeys
    return k1, k2

# Define a function to encrypt a message
def encrypt(N, k1, k2, pi):
    # Define a permutation P
    P = [2, 0, 1, 3]
    # Apply the user-defined shift order pi to the message N
    N = [N[pi[i]] for i in range(8)]
    # Split N into two halves: G0 and D0
    G0 = N[:4]
    D0 = N[4:]
    # XOR each element of G0 with the corresponding element of k1 and apply the permutation P to get D1
    D1 = [P[G0[i]] ^ k1[i] for i in range(4)]
    # OR each element of G0 with the corresponding element of k1 and XOR it with D0 to get G1
    G1 = [D0[i] ^ (G0[i] | k1[i]) for i in range(4)]
    # XOR each element of G1 with the corresponding element of k2 and apply the permutation P to get D2
    D2 = [P[G1[i]] ^ k2[i] for i in range(4)]
    # OR each element of G1 with the corresponding element of k2 and XOR it with D1 to get G2
    G2 = [D1[i] ^ (G1[i] | k2[i]) for i in range(4)]
    # Concatenate G2 and D2 to get the encrypted message C
    C = G2 + D2
    # Compute the inverse permutation of pi
    pi_inv = [pi.index(i) for i in range(8)]
    # Apply pi_inv to C to get the final encrypted message
    C = [C[pi_inv[i]] for i in range(8)]
    return C

# Define a function to decrypt an encrypted message
def decrypt(C, k1, k2, pi):
    # Define the inverse permutation of P
    P_inv = [3 ,2 ,0 ,1]

    # Apply the user-defined shift order pi to the encrypted message C
    C = [C[pi[i]] for i in range(8)]
    # Split C into two halves: G2 and D2
    G2 = C[:4]
    D2 = C[4:]
    # XOR each element of D2 with the corresponding element of k2 and apply the inverse permutation P_inv to get G1
    G1 = [P_inv[D2[i] ^ k2[i]] for i in range(4)]
    # OR each element of G1 with the corresponding element of k2 and XOR it with G2 to get D1
    D1 = [G2[i] ^ (G1[i] | k2[i]) for i in range(4)]
    # XOR each element of D1 with the corresponding element of k1 and apply the inverse permutation P_inv to get G0
    G0 = [P_inv[D1[i] ^ k1[i]] for i in range(4)]
    # OR each element of G0 with the corresponding element of k1 and XOR it with G1 to get D0
    D0 = [G1[i] ^ (G0[i] | k1[i]) for i in range(4)]
    # Concatenate G0 and D0 to get the decrypted message N
    N = G0 + D0
    # Compute the inverse permutation of pi
    pi_inv = [pi.index(i) for i in range(8)]
    # Apply pi_inv to N to get the final decrypted message
    N = [N[pi_inv[i]] for i in range(8)]
    return N

# Define a function to convert a string to a list of integers
def string_to_int_list(s):
    return [ord(c) for c in s]

# Define a function to convert a list of integers to a string
def int_list_to_string(l):
    return ''.join([chr(i) for i in l])

# Prompt the user to enter the values for K, H, pi, and N as text
K_input = input("Please enter the values of K: (K is the key used to generate the subkeys) separated by spaces: ")
K = string_to_int_list(K_input)

H_input = input("Please enter the values of H: (H is the user-defined permutation used) separated by spaces: ")
H = list(map(int,H_input.split()))

pi_input = input("Please enter the values of pi: (pi is the user-defined shift order used) separated by spaces: ")
pi = list(map(int,pi_input.split()))

N_input = input("Please enter the values of N: (N is the message to be encrypted): ")
N = string_to_int_list(N_input)

# Generate the subkeys using the generate_keys function
k1,k2=generate_keys(K,H,[2, 0, 1, 3])
# Print the subkeys as text
print("Subkeys:", int_list_to_string(k1), int_list_to_string(k2))

# Encrypt the message using the encrypt function
C=encrypt(N,k1,k2,pi)
# Print the encrypted message as text
print("Encrypted message:", int_list_to_string(C))

# Decrypt the encrypted message using the decrypt function
N=decrypt(C,k1,k2,pi)
# Print
