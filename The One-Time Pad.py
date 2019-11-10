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
        key.append(random.randint(0,26))
    print(key)

    x = []
    for i in range(length):
        if alphanumeric_numbers[i] != -65:
            x.append(alphanumeric_numbers[i] + key[i])
        else:
            x.append(-65)
    print(x)


    # # convert from alphanumeric scale to encrypted ASCII numerals
    # for i in range(length):
    #     if encrypted_numbers[i] == -65:
    #         encrypted_numbers[i] = 32
    #     else:
    #         encrypted_numbers[i] = encrypted_numbers[i] % 26 + 97
    #
    # # convert from ASCII numerals to corresponding characters
    # encrypted_letters = ''.join(chr(i) for i in encrypted_numbers)
    # return (encrypted_letters)
encrypt(text)

    # while shift.isnumeric() == False:
    #     print("Please enter a number for the shift:")
    #     shift = input()
    #
    # shift = int(shift) % 26
    #
    # alphanumeric_numbers = []
    # encrypted_numbers = []
    #
    # # change ASCII numbers to alphanumeric numbers
    # for n in range(length):
    #     a = text[n]
    #     alphanumeric_numbers.append(ord(a) - 97)
    #
    # # exclude whitespaces from encryption
    # for x in alphanumeric_numbers:
    #     if x != -65:
    #         encrypted_numbers.append(x + shift)
    #     else:
    #         encrypted_numbers.append(-65)
    #
    # # convert from alphanumeric scale to encrypted ASCII numerals
    # for i in range(length):
    #     if encrypted_numbers[i] == -65:
    #         encrypted_numbers[i] = 32
    #     else:
    #         encrypted_numbers[i] = encrypted_numbers[i] % 26 + 97
    #
    # # convert from ASCII numerals to corresponding characters
    # encrypted_letters = ''.join(chr(i) for i in encrypted_numbers)
    # return (encrypted_letters)
