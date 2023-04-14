def generate_keys(K, H, P):
    # Apply the user-defined permutation H to the key K
    K = [K[H[i]] for i in range(8)]
    # Divide K into two blocks of 4 bits
    k1_prime = K[:4]
    k2_prime = K[4:]
    # Generate k1 by XORing k1_prime and k2_prime
    k1 = [k1_prime[i] ^ k2_prime[i] for i in range(4)]
    # Generate k2 by ANDing k2_prime and k1_prime
    k2 = [k2_prime[i] & k1_prime[i] for i in range(4)]
    # Rotate k1 to the left by two positions
    k1 = k1[2:] + k1[:2]
    # Rotate k2 to the right by one position
    k2 = [k2[-1]] + k2[:-1]
    # Return the two subkeys
    return k1, k2

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

# Prompt the user to input the values for K, H, pi, and N
K_input = input("Please enter the values of K: (K is the key used to generate the subkeys) separated by spaces: ")
K = list(map(int,K_input.split()))

H_input = input("Please enter the values of H: (H is the user-defined permutation used) separated by spaces: ")
H = list(map(int,H_input.split()))

pi_input = input("Please enter the values of pi: (pi is the user-defined shift order used) separated by spaces: ")
pi = list(map(int,pi_input.split()))

N_input = input("Please enter the values of N: (N is the message to be encrypted) separated by spaces: ")
N = list(map(int,N_input.split()))

# Generate the subkeys using the generate_keys function
k1,k2=generate_keys(K,H,[2, 0, 1, 3])
# Print the subkeys
print("Subkeys:", k1,k2)

# Encrypt the message using the encrypt function
C=encrypt(N,k1,k2,pi)
# Print the encrypted message
print("Encrypted message:", C)

# Decrypt the encrypted message using the decrypt function
N=decrypt(C,k1,k2,pi)
# Print the decrypted message
print("Decrypted message:", N)
