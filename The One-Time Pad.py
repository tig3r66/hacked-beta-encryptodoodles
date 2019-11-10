# This is the One-Time Pad

import random
text = input("Enter code: ")

# for encrypting text
def encrypt(text):
    length = len(text)

    alphanumeric_numbers = []
    # change ASCII numbers to alphanumeric numbers
    for n in range(length):
        a = text[n]
        alphanumeric_numbers.append(ord(a) - 97)
    print(alphanumeric_numbers)

    key = []
    # shift conditions, convert to integer
    for n in range(length):
        key.append(random.randint(0,25))
    print(key)

    x = []
    for i in range(length):
        if alphanumeric_numbers[i] != -65:
            x.append((alphanumeric_numbers[i] + key[i])%26 + 97)
        else:
            x.append(-65+97)
    print(x)

    # convert from ASCII numerals to corresponding characters
    encrypted_letters = ''.join(chr(i) for i in x)
    print(encrypted_letters)


    def decrypt(encrypted_letters, key, length):

    # Convert encrypted_letters to ASCII values
        alphanumeric_numbers = []
        for i in range(length):
            alphanumeric_numbers.append(ord(encrypted_letters[i]))
        print(alphanumeric_numbers)

    # Subtract key from ASCII values
        x = []
        for i in range(length):
            if alphanumeric_numbers[i] != 32:
                if alphanumeric_numbers[i] - key[i]-97 < 0:
                    x.append(alphanumeric_numbers[i] - key[i]-97+26)
                else:
                    x.append(alphanumeric_numbers[i] - key[i]-97)
            else:
                x.append(-65)
        print(x)


    decrypt(encrypted_letters, key, length)

encrypt(text)

