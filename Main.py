import pyperclip
import Enigma
import Caesar
import Readtxt
import Vigenere
import playfair
import importlib
# import AES


def get_text_type():
    text_type = input('\nOption 1: you have a .txt file to encrypt/decrypt\n'
        'Option 2: you wish to enter a message to encrypt/decrypt\n'
        'Enter 1 or 2: ')
    while (text_type.isdigit() is False) or (int(text_type) < 0) or (int(text_type) > 5):
        print("\nInvalid selection. Please try again.")
        text_type = input('Option 1: you have a .txt file to encrypt/decrypt\n'
        'Option 2: you wish to enter a message to encrypt/decrypt\n'
        'Enter 1 or 2: ')
    return int(text_type)


def get_cypher_type():
    CypherType = input('Option 1: encryption\nOption 2: decryption\n'
                       'Enter 1 or 2: ')
    while (CypherType.isdigit() is False) or (int(CypherType) < 0) or (int(CypherType) > 5):
        print("\nInvalid selection. Please try again.")
        CypherType = input('Option 1: encryption\nOption 2: decryption\n'
                           'Enter 1 or 2: ')
    return int(CypherType)


def get_encryption_type():
    encryptionType = input("Enter a cipher option number: ")
    while ((encryptionType.isdecimal() is False)
        or (int(encryptionType) < 0 or int(encryptionType) > 5)):
            print("Invalid input.")
            encryptionType = input("Enter a cipher option number: ").strip()
    return int(encryptionType)


if __name__ == '__main__':
    flag =  True
    while flag:
        # asks user for decryption or encryption
        CypherType = get_cypher_type()
        # FOR ENCRYPTION
        if CypherType == 1:
            TextType = get_text_type()
            if TextType == 1:
                filename = input('Plaintext filename: ')
                text = Readtxt.readtxt(filename)
            else:
                text = input('\nInput the message you want to encrypt: ')
        # FOR DECRYPTION
        elif CypherType == 2:
            TextType = get_text_type()
            if TextType == 1:
                filename = input('Plaintext filename: ')
                text = Readtxt.readtxt(filename)
            else:
                text = input('\nInput the message you want to decrypt: ')

        # Clean up text
        text = text.replace('\n', ' ').lower()
        whitelist = 'abcdefghijklmnopqrstuvwxyz '
        text = ''.join(filter(whitelist.__contains__, text))

        # picking the encryption method
        encryption_dict = {1: 'Caesar', 2: 'Vigenere', 3: 'Enigma',
                           4: 'AES', 5: 'playfair'}
        print('\nCipher Options')
        for k, v in encryption_dict.items():
            print(f'  {k}: {v}')

        encryptionType = get_encryption_type()
        encryptionTypeVal = importlib.import_module(encryption_dict[encryptionType])
        if CypherType == 1:
            output = encryptionTypeVal.encrypt(text)
        else:
            output = encryptionTypeVal.decrypt(text)

        pyperclip.copy(output)
        print(f'\nOutput: {output}\nThe text has been copied to your clipboard :)')

        cont = input('Want to continue? [Y/N]: ').upper().strip()
        if cont != 'Y':
            flag = False
