# This is a Caesar Cipher
y=5%25
import numpy

word = input("Enter your code: ")
shift = input("Enter shift number: ")
shift = int(shift)
length = len(word)
encrypted_num =[]
for n in range(length):
    a = word[n]
    encrypted_num.append(ord(a) - 97)
# print(encrypted_num)
# Letters are now from 0 to 25 and space is -65
array=numpy.array(encrypted_num)
encrypted_nums = array + shift + 97
apple = ''.join(chr(i) for i in encrypted_nums)
print(apple)

