# This is the One-Time Pad

import random
text = input("Enter code: ")


# for coding text
def crypt(text):

    length = len(text)
    alphanumerical_numbers = []

    # change text letters to alphanumeric numbers
    for n in range(length):
        text_letters = text[n]
        alphanumerical_numbers.append(ord(text_letters) - 97)

    # print(alphanumerical_numbers)

    key = []

    # random key generator
    for n in range(length):
        key.append(random.randint(0,25))

    # print(key)

    ascii_values = []

    # space condition, convert to ASCII values
    for i in range(length):
        if alphanumerical_numbers[i] != -65:
            ascii_values.append((alphanumerical_numbers[i] + key[i])%26 + 97)
        else:
            ascii_values.append(-65+97)

    # print(x)

    # convert from ASCII values to corresponding characters
    encrypted_letters = ''.join(chr(i) for i in ascii_values)
    print(encrypted_letters)

    # code for decrypting text
    def decrypt(encrypted_letters, key, length):

        # Convert encrypted_letters to ASCII values
        ascii_values = []
        for i in range(length):
            ascii_values.append(ord(encrypted_letters[i]))
        # print(ascii_values)

        # Subtract key from ASCII values, convert to decrypted alphanumerical
        decrypted_alphanumerical = []
        for i in range(length):
            if ascii_values[i] != 32:
                if ascii_values[i] - key[i]-97 < 0:
                    decrypted_alphanumerical.append(ascii_values[i] - key[i]-97+26)
                else:
                    decrypted_alphanumerical.append(ascii_values[i] - key[i]-97)
            else:
                decrypted_alphanumerical.append(-65)
        # print(decrypted_alphanumerical)

        # Convert
        for i in range(length):
            decrypted_alphanumerical[i] = decrypted_alphanumerical[i]+97
        # print(decrypted_alphanumerical)

        for i in range(length):
            decrypted_letters = ''.join(chr(i) for i in decrypted_alphanumerical)
        print(decrypted_letters)

        #convert from ASCII values to letters
    decrypt(encrypted_letters, key, length)

crypt(text)

