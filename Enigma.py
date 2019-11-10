import random


random.seed(0)
#make each rotor
rotor = [
    [random.randint(1, 26) for i in range(26)],
    [random.randint(1, 26) for i in range(26)],
    [random.randint(1, 26) for i in range(26)],
    [random.randint(1, 26) for i in range(26)],
    [random.randint(1, 26) for i in range(26)]
]


#function to do caesar cipher
def shiftletter(shift, letter):
    #convert all letters to lowercase
    lower_letter = letter.lower()

    #make sure to code for the space case
    if ord(lower_letter) == 32:
        new_letter = ' '
    else:
        #change shift the number on the alphanumeric scale
        shift_num = (ord(lower_letter) + shift - 96) % 26
        #letter z is 26, not 0
        if shift_num == 0:
            shift_num = 26
        #change the shift back into a letter
        new_letter = chr(shift_num + 96)
    return(new_letter)


#finds the mod_position
def list_to_mod(position_list):
    initial_num = position_list[0] * 26 * 26 + position_list[1] * 26 + position_list[2] + 1
    return initial_num


#find the shift for every key
def mod_to_list(initial_num):
    new_list = []
    new_list.append(initial_num // (26 * 26))
    initial_num -= (initial_num // (26 * 26)) * (26 * 26)
    new_list.append(initial_num // 26)
    initial_num -= (initial_num // (26) * (26))
    new_list.append(initial_num)
    return new_list


#finds the shift key based on the enigma positions
def list_to_key(newlist,rotor_order):
    key = (rotor[rotor_order[0]][newlist[0]] + rotor[rotor_order[1]][newlist[1]] +
           rotor[rotor_order[2]][newlist[2]]) % 26
    return key


def get_valid_rotor_input():
    rotor_ord = int(input('Pick rotor 1, between 1 and 5: ')) - 1
    while not ((0 < rotor_ord) and (rotor_ord < 6)):
        print("Input must lie in the range [1, 5].")
        rotor_ord = int(input('Pick rotor 1, between 1 and 5: ')) - 1
    return rotor_ord


def encrypt(text):
    # user input rotor ordering
    rotor_order = [0, 0, 0]
    rotor_order[0] = get_valid_rotor_input()
    rotor_order[1] = get_valid_rotor_input()
    rotor_order[2] = get_valid_rotor_input()

    # user input the rotor positions
    initial_pos = [0, 0, 0]
    initial_pos[0] = int(input('What is position of the first rotor? Between 1 and 26: ')) - 1
    initial_pos[1] = int(input('What is position of the second rotor? Between 1 and 26: ')) - 1
    initial_pos[2] = int(input('What is position of the third rotor? Between 1 and 26: ')) - 1

    # initialize the encrypted text
    new_word = ''
    for letter in text:
        initial_num = list_to_mod(initial_pos)
        initial_pos = mod_to_list(initial_num)
        key = list_to_key(initial_pos, rotor_order)
        new_word += shiftletter(key, letter)
    return new_word


def decrypt(text):
    # user input rotor ordering
    rotor_order = [0, 0, 0]
    rotor_order[0] = get_valid_rotor_input()
    rotor_order[1] = get_valid_rotor_input()
    rotor_order[2] = get_valid_rotor_input()

    # user input the rotor positions
    initial_pos = [0, 0, 0]
    initial_pos[0] = int(input('What is position of the first rotor? Between 1 and 26: ')) - 1
    initial_pos[1] = int(input('What is position of the second rotor? Between 1 and 26: ')) - 1
    initial_pos[2] = int(input('What is position of the third rotor? Between 1 and 26: ')) - 1

    # initialize the encrypted text
    new_word = ''
    for letter in text:
        initialnum = list_to_mod(initial_pos)
        # print(initialnum)
        initial_pos = mod_to_list(initialnum)
        # print(initial_pos)
        key = list_to_key(initial_pos, rotor_order)
        # print(key)
        new_word += shiftletter(key * (-1), letter)
    return new_word


if __name__ == '__main__':
    user_in = input()
    print(encrypt(user_in))
