import Enigma
import Caesar
import Readtxt
import AES



#asks user for decryption or encryption
CypherType = input('Enter 1 for encryption, enter 2 for decryption: ')

#FOR ENCRYPTION
if CypherType == 1:
    TextType = input('Enter 1 if you have the .txt file, enter 2 for onscreen message: ')
    #For txt
    if TextType ==1:
        filename = input('What is the filename of the txt')



#FOR DECRYPTION
if CypherType == 2: