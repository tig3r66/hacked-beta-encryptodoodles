# This is a Caesar Cipher

text = input("Enter your code: ")
text = text.lower()
shift = input("Enter shift number: ")
shift = int(shift) % 26
length = len(text)

def encrypt(text):
    import numpy
    encrypted_num = []
    for n in range(length):
        a = text[n]
        encrypted_num.append(ord(a) - 97)

    encrypted_nums = []
    for x in encrypted_num:
        if x != -65:
            encrypted_nums.append(x+shift)
        else:
            encrypted_nums.append(-65)
    for i in range(length):
        encrypted_nums[i] = encrypted_nums[i]%26 + 97
        if encrypted_nums[i] == 110:
            encrypted_nums[i]=32

    encrypted_letters = ''.join(chr(i) for i in encrypted_nums)
    print(encrypted_letters)
encrypt(text)

def decrypt(text):
    import numpy
    decrypted_num = []
    for n in range(length):
        a = text[n]
        decrypted_num.append(ord(a) - 97)

    decrypted_nums = []
    for x in decrypted_num:
        if x != -65:
            decrypted_nums.append(x - shift)
        else:
            decrypted_nums.append(-65)

    for i in range(length):
        decrypted_nums[i] = decrypted_nums[i]%26 + 97
        if decrypted_nums[i] == 110:
            decrypted_nums[i] = 32

    decrypted_letters = ''.join(chr(i) for i in decrypted_nums)
    print(decrypted_letters)

decrypt(text)
