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

#make each rotor
rotor = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
]

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

def list_to_key(newlist):
    key = (rotor[roto_order[0]][newlist[0]] + rotor[roto_order[1]][newlist[1]] +
           rotor[roto_order[2]][newlist[2]])%26
    return key

text = 'aaaaa'
roto_order = [1,2,3]

initial_pos = [0, 0, 0]
newword = ''

for letter in text:
    initialnum = list_to_mod(initial_pos)
    #print(initialnum)
    initial_pos = mod_to_list(initialnum)
    #print(initial_pos)
    key = list_to_key(initial_pos)
    #print(key)
    newword += shiftletter(key, letter)


print(newword)


