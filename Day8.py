# Day 8 Caesar cipher, functions with inputs, arguments & parameters

# def greet():
#     print("Hello")
#     print("there")
#     print("obi wan")
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
# greet_with_name("Niloy")

# def greet_with_name_and_location(name, location):
#     print(f"Hello {name} from {location}")
# greet_with_name_and_location("Niloy", "Dhaka")

# Exercise 8.1
# import math
# def print_calc(height, width, cover):
#     print(math.ceil(height*width/cover))
# test_h = int(input("Height of wall:"))
# test_w = int(input("Width of wall:"))
# coverage = 5
# print_calc(height=test_h, width= test_w, cover= coverage)

# Exercise 8.2

# def prime_checker(number):
#     d = {}
#     i = 2
#     while i*i<=number:
#         for j in range(2*i, number+1, i):
#             d[j] = True
#         if i == 2:
#             i+=1
#         else:
#             i+=2
#     if number in d:
#         print("False")
#     else:
#         print("True")

# while True:
#     n = int(input("Check this number: "))
#     prime_checker(number=n)

# Exercise 8.3 Encode a text
# alphabet = [chr(ord('a')+i) for i in range(26)]*2
# def encode(mess, shift):
#     cipher_text = ""
#     for letter in mess:
#         cipher_text += alphabet[alphabet.index(letter) + shift]
#     return cipher_text
# def decode(enc_mess, shift):
#     text = ""
#     for enc_letter in enc_mess:
#         text += alphabet[ alphabet.index(enc_letter) - shift]
#     return text

# mess = "abcdefghijklmnopqrstuvwxyz"
# shift = 2
# print(decode(encode(mess, shift), shift))

# Exercise 8.4 + 8.5 Single function + UX Experience

from Day8_art import logo
alphabet = [chr(ord('a')+i) for i in range(26)]*2
def caesar(mess, shift, type):
    text = ""
    if type == 'decode':
        shift *= -1
    for letter in mess:
        if letter not in alphabet:
            text += letter
        else:
            text += alphabet[alphabet.index(letter) + shift]
    return text

print(logo)
while True:
    print("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
    op = input().lower()
    print("Type your message:")
    mess = input()
    print("Type your shift number:")
    shift = int(input())
    print(caesar(mess, shift, op))
    print('Type "yes" to go again, or "no" to exit')
    ans = input().lower()
    if ans != "yes":
        break
# Day 8 project
# from Day8_art import logo
# encoding_alphabet = [chr(ord('a')+i) for i in range(26)]
# def encode_message(message, shift_number):
#     if shift_number%26 == 0:
#         shift_number += 13
#     shift_number %= 26
#     encoded_message = ""
#     for letter in message:
#         if letter not in encoding_alphabet:
#             encoded_message += letter
#         else:
#             cipher_letter = encoding_alphabet[(ord(letter) - ord('a') + shift_number) % 26] 
#             encoded_message += cipher_letter
#     return encoded_message
# '''
# 0 1 2 3 4 5
# a b c d e f
# b c d e f a

# ord(letter) - ord('a')
# '''
# def decode_message(encoded_message, shift_number):
#     if shift_number%26 == 0:
#         shift_number += 13
#     shift_number %= 26
#     decoded_message = ""
#     for cipher_letter in encoded_message:
#         if cipher_letter not in encoding_alphabet:
#             decoded_message += cipher_letter
#         else:
#             original_letter = encoding_alphabet[( 26 + ord(cipher_letter) - ord('a') - shift_number) % 26 ]
#             decoded_message += original_letter
#     return decoded_message

# print(logo)
# while True:
#     print("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
#     op = input().lower()
#     if op == 'encode':
#         print("Type your message:")
#         message = input()
#         print("Type the shift number:")
#         shift_number = int(input())
#         encoded_message = encode_message(message, shift_number)
#         print("Here's the encoded message: " + encoded_message)
#     elif op == 'decode':
#         print("Type your encoded message:")
#         encoded_message = input()
#         print("Type the shift number:")
#         shift_number = int(input())
#         decoded_message = decode_message(encoded_message, shift_number)
#         print("Here's the decoded message: " + decoded_message)
#     print("Type 'yes' if you want to go again, else type 'no'")
#     choice = input().lower()
#     if choice != 'yes':
#         break
        