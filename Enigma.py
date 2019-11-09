#make each rotor
rotor = [
    [15, 3, 25, 22, 12, 24, 1, 18, 5, 8, 23, 10, 16, 7, 20, 11, 17, 14, 6, 26, 9, 21, 2, 13, 19, 4],
    [8, 10, 13, 21, 15, 23, 12, 22, 16, 1, 17, 24, 18, 20, 2, 5, 26, 4, 3, 9, 25, 11, 6, 19, 14, 7],
    [6, 9, 10, 7, 19, 20, 12, 4, 3, 13, 24, 5, 25, 2, 11, 8, 21, 23, 26, 14, 16, 17, 15, 18, 1, 22],
    [23, 13, 1, 20, 7, 10, 15, 18, 4, 8, 11, 19, 17, 14, 5, 6, 16, 26, 25, 2, 21, 12, 22, 9, 24, 3],
    [22, 17, 20, 9, 7, 4, 8, 13, 12, 5, 26, 21, 24, 25, 19, 16, 14, 11, 10, 2, 1, 18, 23, 15, 3, 6],
]

#function to do caesar cipher
def shiftletter(shift, letter):
    #convert all letters to lowercase
    lowerletter = letter.lower()

    #make sure to code for the space case
    if ord(lowerletter) == 32:
        newletter = ' '
    else:
        #change shift the number on the alphanumeric scale
        shiftnum = (ord(lowerletter) + shift - 96)%26

        #letter z is 26, not 0
        if shiftnum == 0:
            shiftnum = 26

        #change the shift back into a letter
        newletter = chr(shiftnum + 96)
    return(newletter)

#finds the mod_position
def list_to_mod(position_list):
    initialnum = position_list[0]*26*26 + position_list[1]*26 + position_list[2] + 1
    return initialnum

#find the shift for every key
def mod_to_list(initialnum):
    newlist = []
    newlist.append(initialnum//(26*26))
    initialnum -= (initialnum//(26*26))*(26*26)
    newlist.append(initialnum // 26)
    initialnum -= (initialnum//(26)*(26))
    newlist.append(initialnum)
    return newlist

#finds the shift key based on the enigma positions
def list_to_key(newlist,rotor_order):
    key = (rotor[rotor_order[0]][newlist[0]] + rotor[rotor_order[1]][newlist[1]] +
           rotor[rotor_order[2]][newlist[2]])%26
    return key

def encrypt(text):
    # user input rotor ordering
    rotor_order = [0, 0, 0]
    rotor_order[0] = int(input('Pick rotor 1, between 1 and 5: '))
    rotor_order[1] = int(input('Pick rotor 2, between 1 and 5: '))
    rotor_order[2] = int(input('Pick rotor 3, between 1 and 5: '))

    # user input the rotor positions
    initial_pos = [0, 0, 0]
    initial_pos[0] = int(input('What is position of the first rotor? Between 1 and 26: '))
    initial_pos[1] = int(input('What is position of the second rotor? Between 1 and 26: '))
    initial_pos[2] = int(input('What is position of the third rotor? Between 1 and 26: '))

    # initialize the encrypted text
    newword = ''

    for letter in text:
        initialnum = list_to_mod(initial_pos)
        # print(initialnum)
        initial_pos = mod_to_list(initialnum)
        # print(initial_pos)
        key = list_to_key(initial_pos, rotor_order)
        # print(key)
        newword += shiftletter(key, letter)
    return newword


def decrypt(text):
    # user input rotor ordering
    rotor_order = [0, 0, 0]
    rotor_order[0] = int(input('Pick rotor 1, between 1 and 5: '))
    rotor_order[1] = int(input('Pick rotor 2, between 1 and 5: '))
    rotor_order[2] = int(input('Pick rotor 3, between 1 and 5: '))

    # user input the rotor positions
    initial_pos = [0, 0, 0]
    initial_pos[0] = int(input('What is position of the first rotor? Between 1 and 26: '))
    initial_pos[1] = int(input('What is position of the second rotor? Between 1 and 26: '))
    initial_pos[2] = int(input('What is position of the third rotor? Between 1 and 26: '))

    # initialize the encrypted text
    newword = ''

    for letter in text:
        initialnum = list_to_mod(initial_pos)
        # print(initialnum)
        initial_pos = mod_to_list(initialnum)
        # print(initial_pos)
        key = list_to_key(initial_pos, rotor_order)
        # print(key)
        newword += shiftletter(key * -1, letter)
    return newword

type = input('what do you want to do, type 1 for encryption, type 2 for decryption: ')
if type == '1':
    print(encrypt(input('What is the unencrypted message? ')))
elif type == '2':
    print(decrypt(input('What is the encrypted message? ')))
else:
    print('you are bad')

