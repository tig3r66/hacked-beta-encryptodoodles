#This is the Vigener Cipher

text = input('message to encode: ')
shift = int(input('enter shift: '))

#function to do caesar cipher
def encrypt()
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

newword = ''
for letter in text:
    newletter = shiftletter(shift, letter)
    newword = newword + newletter

print(newword)

encrypt()