import math

def rail_fence_encrypt(message, key):
    message = message.upper()
    message = message.replace(" ", "")
    encrypted_message = ""

    print("message length = ", len(message))

    rails = ['' for _ in range(key)]

    # Determine the rail for each character based on its position
    period = 2*(key-1)

    for i, char in enumerate(message):
        r = i % period
        rail = r if r < key else period - r
        rails[rail] += char

    encrypted_message = encrypted_message.join(rails)
            #encrypted_message = message[ : pos] + letter + message[ pos : ]
    return encrypted_message

def rail_fence_decrypt(cipher, key):
    decrypted_message = ""
    rails = []

    cipher_len = len(ciphertext)
    period = 2*(key-1)

    for i in range(cipher_len):
        remainder = i % period
        if remainder < key:
            rail = remainder
        else:
            rail = period - remainder
        rails.append(rail)

    rail_counts = [0]*key
    for rail in rails:
        rail_counts[rail] += 1

    rail_slices = {}
    index = 0
    for rail in range(key):
        count = rail_counts[rail]
        rail_slices[rail] = list(ciphertext[index:index + count])
        index += count

    for rail in rails:
        decrypted_message += rail_slices[rail].pop(0)

    return decrypted_message



ciphertext = rail_fence_encrypt("This is a test",5)
decrypted = rail_fence_decrypt(ciphertext,5)
print("This is a test")
print(ciphertext)
print(decrypted)