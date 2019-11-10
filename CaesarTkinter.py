# This is a Caesar Cipher
import numpy

# for encrypting text
def encrypt(text, shift):
    length = len(text)
    while shift.isnumeric() == False:
        print("Please enter a number for the shift:")
        shift = input("Enter shift: ")

    shift = int(shift) % 26

    alphanumeric_numbers = []
    encrypted_numbers = []
    # change ASCII numbers to alphanumeric numbers
    for n in range(length):
        a = text[n]
        alphanumeric_numbers.append(ord(a) - 97)

    # exclude whitespaces from encryption
    for x in alphanumeric_numbers:
        if x != -65:
            encrypted_numbers.append(x + shift)
        else:
            encrypted_numbers.append(-65)

    # convert from alphanumeric scale to encrypted ASCII numerals
    for i in range(length):
        if encrypted_numbers[i] == -65:
            encrypted_numbers[i] = 32
        else:
            encrypted_numbers[i] = encrypted_numbers[i] % 26 + 97

    # convert from ASCII numerals to corresponding characters
    encrypted_letters = ''.join(chr(i) for i in encrypted_numbers)
    return (encrypted_letters)


# for decrypting text
def decrypt(text,shift):
    length = len(text)

    while shift.isnumeric() == False:
        shift = input("Shift: ")

    shift = int(shift) % 26

    alphanumeric_numbers = []
    decrypted_numbers = []
    # change ASCII numbers to alphanumeric numbers
    for n in range(length):
        a = text[n]
        alphanumeric_numbers.append(ord(a) - 97)

    # exclude whitespaces from encryption
    for x in alphanumeric_numbers:
        if x != -65:
            decrypted_numbers.append(x - shift)
        else:
            decrypted_numbers.append(-65)

    # convert from alphanumeric scale to encrypted ASCII numerals
    for i in range(length):
        if decrypted_numbers[i] == -65:
            decrypted_numbers[i] = 32
        else:
            decrypted_numbers[i] = decrypted_numbers[i] % 26 + 97

    # convert from ASCII numerals to corresponding characters
    decrypted_letters = ''.join(chr(i) for i in decrypted_numbers)
    return (decrypted_letters)
