import pyperclip
import Enigma
import Caesar
import Readtxt
import Vigenere
import playfair
# import AES

if __name__ == '__main__':
    flag =  True
    while flag:
        #asks user for decryption or encryption
        CypherType = input('Option 1: encryption\nOption 2: decryption\n'
                           'Please enter either 1 or 2: ')


        #FOR ENCRYPTION
        if CypherType == '1':
            TextType = input('Enter 1 if you have the .txt file, enter 2 for onscreen message: ')
            #For txt
            if TextType == '1':
                filename = input('What is the filename of the txt? ')
                text = Readtxt.readtxt(filename)
            elif TextType == '2':
                text = input('Input the message you want to encrypt: ')
        #FOR DECRYPTION
        elif CypherType == '2':
            TextType = input('Enter 1 if you have the .txt file, enter 2 for onscreen message: ')
            #For txt
            if TextType == '1':
                filename = input('What is the filename of the txt? ')
                text = Readtxt.readtxt(filename)
            elif TextType == '2':
                text = input('Input the message you want to decrypt: ')
        else:
            print('you are bad')
            exit()


        #Clean up text
        text = text.replace('\n', ' ').lower()
        whitelist = 'abcdefghijklmnopqrstuvwxyz '
        text = ''.join(filter(whitelist.__contains__, text))

        #picking the encryption method
        print('''
        Enter the encryption of choice:
        1 - Caesar
        2 - Vigenere
        3 - Enigma
        4 - AES
        5 - Playfair
        ''')
        encryptionType = input()

        if encryptionType == '1':
            if CypherType == '1':
                output = Caesar.encrypt(text)
                print(output)
            elif CypherType == '2':
                output = Caesar.decrypt(text)
                print(output)
        elif encryptionType == '2':
            if CypherType == '1':
                output = Vigenere.encrypt()
                print(output)
            elif CypherType == '2':
                output = Vigenere.decrypt()
                print(output)
        elif encryptionType == '3':
            if CypherType == '1':
                output = Enigma.encrypt(text)
                print(output)
            elif CypherType == '2':
                output = Enigma.decrypt(text)
                print(output)
        elif encryptionType == '4':
            AES.AES(text, CypherType)
        elif encryptionType == '5':
            if CypherType == '1':
                output = playfair.encrypt(text)
                print(output)
            elif CypherType == '2':
                output = playfair.decrypt(text)
                print(output)
        else:
            print('you are bad')
        pyperclip.copy(output)
        print('The text has been copied to your clipboard :)')

        cont = input('Want to continue? [Y/N]: ').upper().strip()
        if cont != 'Y':
            flag = False
