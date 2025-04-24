import random
import math


def prime_check(num):
    if num < 2:
        return False
    for i in range(2,(num//2) +1):
        if num % i == 0:
            return False
    return True

def prime_gen(min_val,max_val):
    rand_num = random.randint(min_val,max_val)
    while not prime_check(rand_num):
        rand_num = random.randint(min_val,max_val)
    return rand_num

def inverse_mod(e, phi):
    for d in range(3,phi):
        if (d * e) % phi == 1:
            return d
    return -1

p = prime_gen(1000,5000)
q = prime_gen(1000,5000)

while p==q:
    q = prime_gen(1000,5000)

n = p * q
phi_n = (p-1) * (q-1)

e = random.randint(3, phi_n-1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3,phi_n - 1)

d = inverse_mod(e, phi_n)

print("Public Key: ", d)
print("Private Key: ", e)
print("N: ",n)
print("Phi of N: ", phi_n)
print("P: ", p)
print("Q: ", q)

message = "This is a test"

message_encoded = [ord(c) for c in message]

ciphertext = [pow(c,e,n) for c in message_encoded]

xor_ciphertext = [c^d for c in ciphertext]

print(xor_ciphertext)
print(ciphertext)

xor_deciphered_test = [c^d for c in xor_ciphertext]
xor_encoded = [pow(ch,d,n) for ch in xor_deciphered_test]

xor_message = "".join(chr(ch) for ch in xor_encoded)

message_encoded = [pow(ch,d,n) for ch in ciphertext]

message = "".join(chr(ch) for ch in message_encoded)

print(xor_message)
print(message)
