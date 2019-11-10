# This is the Vigener Cipher

# Prompt user for code
text = input('enter code: ')

# Prompt user for key, convert to numbers, then convert to alphanumeric scale
keyletter = list(input('enter key: '))
keynumber = [ord(x)-96 for x in keyletter]

# function to do caesar cipher
def shiftletter(shift, letter):

    # convert all letters to lowercase
    lowerletter = letter.lower()

    # make sure to code for the space case
    if ord(lowerletter) == 32:
        newletter = ' '

    else:
        # change shift the number on the alphanumeric scale
        shiftnum = (ord(lowerletter) + shift - 96)%26

        #letter z is 26, not 0
        if shiftnum == 0:
            shiftnum = 26

        # change the shift back into a letter
        newletter = chr(shiftnum + 96)

    return(newletter)

newword =''
spacecount = 0

# relates values in text to values in key using index
for i in range(len(text)):

    
    newletter = shiftletter(keynumber[(i-spacecount) % len(keynumber)], text[i])

    if newletter == ' ':
        spacecount += 1
    newword = newword + newletter
print(newword)
