# This is a Caesar Cipher
import numpy

text = input("Enter your code: ")
text = text.lower()
length = len(text)

shift = input("Enter shift number: ")
while shift.isnumeric() == False:
    print("Please enter a number for the shift:")
    shift = input()

shift = int(shift) % 26


#for encrypting text
def encrypt(text):
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
        if encrypted_nums[i] == -65:
            encrypted_nums[i] = 32
        else:
            encrypted_nums[i] = encrypted_nums[i] % 26 + 97

    encrypted_letters = ''.join(chr(i) for i in encrypted_nums)
    print(encrypted_letters)
encrypt(text)

def decrypt(text):
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
        if decrypted_nums[i] == -65:
            decrypted_nums[i] = 32
        else:
            decrypted_nums[i] = decrypted_nums[i] % 26 + 97

    decrypted_letters = ''.join(chr(i) for i in decrypted_nums)
    print(decrypted_letters)
decrypt(text)
