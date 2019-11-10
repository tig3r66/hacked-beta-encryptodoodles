# This is the substitution cipher
text = input("Enter code: ")

def encrypt():
    length = len(text)

    # Ensure that key is 26 letters and non-repetitive
    key = input("Enter 26 letter non-repetitive key: ")
    key = key.lower()
    while len(key) != 26:
        key = input("Please enter a 26 letter key: ")
    count = 0
    for x in key:
        while key.count(x) != 1:
            key = input("Please enter a non-repetitive key: ")

    # Ensure whitespace stays whitespace
    alphanumeric_num = []
    for i in range(length):
        if ord(text[i]) != 32:
            alphanumeric_num.append(ord(text[i])-97)
        else:
            alphanumeric_num.append(-65)

    # print(alphanumeric_num)

    encrypted_letters = []
    for i in range(length):
        if alphanumeric_num[i] != -65:
            encrypted_letters.append(key[alphanumeric_num[i]])
        else:
            encrypted_letters.append(' ')
    # print(encrypted_letters)

    encrypted_letters = ''.join(encrypted_letters)
    print(encrypted_letters)
# zyxwvutsrqponmlkjihgfedcba
# abcdefghijklmnopqrstuvwxyz

    def decrypt(encrypted_letters, key):
        text=encrypted_letters
        length = len(text)

        # Ensure whitespace stays whitespace
        alphanumeric_num = []
        for i in range(length):
            if ord(text[i]) != 32:
                alphanumeric_num.append(ord(text[i]) - 97)
            else:
                alphanumeric_num.append(-65)

        # print(alphanumeric_num)

        decrypted_letters = []
        for i in range(length):
            if alphanumeric_num[i] != -65:
                decrypted_letters.append(key[alphanumeric_num[i]])
            else:
                decrypted_letters.append(' ')
        # print(decrypted_letters)

        decrypted_letters = ''.join(decrypted_letters)
        print(decrypted_letters)

    decrypt(encrypted_letters, key)

encrypt()