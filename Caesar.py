import math


def caesar_encrypt(message):
    encrypted_message = ""
    message = message.upper()
    message = message.replace(" ", "")

    for i in range(len(message)):
        ascii_num = int.from_bytes(message[i].encode('utf-8'), byteorder='big', signed=False)
        if ascii_num > 64:
            encrypted_num = ((ascii_num-65) + 3)%26
            encrypted_message += chr(encrypted_num+65)
    return encrypted_message

def caesar_decrypt(cipher):
    decrypted_message = ""

    for i in range(len(cipher)):
        ascii_num = int.from_bytes(cipher[i].encode('utf-8'), byteorder='big', signed=False)
        unencrypted_num = ((ascii_num - 65) - 3)
        if unencrypted_num < 0:
            unencrypted_num = 26 + unencrypted_num
        unencrypted_num = unencrypted_num%26
        decrypted_message += chr(unencrypted_num+65)

    return decrypted_message



ciphertext = caesar_encrypt("This is a test")
decrypted = caesar_decrypt(ciphertext)
print(ciphertext)
print(decrypted)