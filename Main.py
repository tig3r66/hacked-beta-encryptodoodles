import Enigma
import Caesar
import Readtxt
#from AES import AES

if __name__ == '__main__':
    flag =  True

    while flag:
        #asks user for decryption or encryption
        CypherType = input('Enter 1 for encryption, enter 2 for decryption: ')

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
                Caesar.encrypt(text)
            elif CypherType == '2':
                Caesar.decrypt(text)
        elif encryptionType == '2':
            if CypherType == '1':
                print('encrypt')
            elif CypherType == '2':
                print('decrypt')
        elif encryptionType == '3':
            if CypherType == '1':
                print(Enigma.encrypt(text))
            elif CypherType == '2':
                print(Enigma.decrypt(text))
        elif encryptionType == '4':
            AES.AES(text, CypherType)
        elif encryptionType == '5':
            if CypherType == '1':
                print('encrypt')
            elif CypherType == '2':
                print('decrypt')

        cont = input('Want to continue? (Y/N)').upper().strip()
        if cont != 'Y':
            flag = False


