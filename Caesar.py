# This is a Caesar Cipher
def encrypt(text):
    import numpy
    word = input("Enter your code: ")
    word = word.lower()
    shift = input("Enter shift number: ")
    shift = int(shift)
    length = len(word)
    encrypted_num =[]
    for n in range(length):
        a = word[n]
        encrypted_num.append(ord(a) - 97)

    encrypted_nums = [x+shift for x in encrypted_num]

    for i in range(length):
         encrypted_nums[i]=encrypted_nums[i]%26 + 97

    encrypted_letters = ''.join(chr(i) for i in encrypted_nums)
    print(encrypted_letters)

def decrypt(text):