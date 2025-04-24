import math
import random

def vigenere_encrypt(message, key):
    key_shift = ""
    message_num = ""
    transposition = []
    encrypted_message = ""
    key = key.upper()
    message = message.upper()
    message = message.replace(" ", "")

    for letter in key:
        ascii_num = int.from_bytes(letter.encode('utf-8'), byteorder='big', signed=False)
        if ascii_num > 90:
            key_shift += str(ascii_num - 97) + " "
            transposition.append(ascii_num-97)
        elif ascii_num > 64:
            key_shift += str(ascii_num - 65) + " "
            transposition.append(ascii_num - 65)

    for i in range(len(message)):
        ascii_num = int.from_bytes(message[i].encode('utf-8'), byteorder='big', signed=False)
        if ascii_num > 64:
            encrypted_num = ((ascii_num-65) + transposition[i%len(transposition)])%26
            message_num += str(encrypted_num) + " "
            encrypted_message += chr(encrypted_num+65)
    return encrypted_message

def vigenere_decrypt(cipher, key):
    key = key.upper()
    transposition = []
    decrypted_message = ""

    for letter in key:
        ascii_num = int.from_bytes(letter.encode('utf-8'), byteorder='big', signed=False)
        transposition.append(ascii_num - 65)

    for i in range(len(cipher)):
        ascii_num = int.from_bytes(cipher[i].encode('utf-8'), byteorder='big', signed=False)
        unencrypted_num = ((ascii_num - 65) - transposition[i % len(transposition)])
        if unencrypted_num < 0:
            unencrypted_num = 26 + unencrypted_num
        unencrypted_num = unencrypted_num%26
        decrypted_message += chr(unencrypted_num+65)

    return decrypted_message

def one_time_pad(message):
    message = message.replace(" ","")
    otp = ""
    for i in range(len(message)):
        otp += chr(random.randint(65,90))

    return otp
pad = one_time_pad("This is a test")
print(pad)
ciphertext = vigenere_encrypt("This is a test",pad)
decrypted = vigenere_decrypt(ciphertext,pad)
print(ciphertext)
print(decrypted)