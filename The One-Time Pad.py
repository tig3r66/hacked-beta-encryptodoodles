# This is the One-Time Pad

import random
text = input("Enter code: ")

# for encrypting text
def encrypt(text):

    length = len(text)
    alphanumeric_numbers = []

    # change ASCII numbers to alphanumeric numbers
    for n in range(length):
        text_letters = text[n]
        alphanumeric_numbers.append(ord(text_letters) - 97)

    # print(alphanumeric_numbers)

    key = []

    # random key generator
    for n in range(length):
        key.append(random.randint(0,25))

    # print(key)

    ascii_values = []

    # space condition, convert to ASCII numerals
    for i in range(length):
        if alphanumeric_numbers[i] != -65:
            ascii_values.append((alphanumeric_numbers[i] + key[i])%26 + 97)
        else:
            ascii_values.append(-65+97)

    # print(x)

    # convert from ASCII numerals to corresponding characters
    encrypted_letters = ''.join(chr(i) for i in ascii_values)
    print(encrypted_letters)

    def decrypt(encrypted_letters, key, length):

        # Convert encrypted_letters to ASCII values
        ascii_values = []
        for i in range(length):
            ascii_values.append(ord(encrypted_letters[i]))
        # print(ascii_values)

    # Subtract key from ASCII values
        x = []
        for i in range(length):
            if ascii_values[i] != 32:
                if ascii_values[i] - key[i]-97 < 0:
                    x.append(ascii_values[i] - key[i]-97+26)
                else:
                    x.append(ascii_values[i] - key[i]-97)
            else:
                x.append(-65)
        # print(x)
        for i in range(length):
            x[i]=x[i]+97
        # print(x)

        for i in range(length):
            decrypted_letters = ''.join(chr(i) for i in x)
        print(decrypted_letters)

        #convert from ASCII values to letters
    decrypt(encrypted_letters, key, length)

encrypt(text)

