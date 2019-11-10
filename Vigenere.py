# This is the Vigenere Cipher

def encrypt():
    """Description: Prompt user for key, convert to numbers, then convert to
    alphanumeric scale
    """
    text = input('Enter code: ').lower()

    key_letter = list(input('Enter key: '))
    key_num = [ord(x)-96 for x in key_letter]

    # function to do caesar cipher
    def shiftletter(shift, letter):
        # convert all letters to lowercase
        lowerletter = letter

        # make sure to code for the space case
        if ord(lowerletter) == 32:
            new_letter = ' '
        else:
            # change shift the number on the alphanumeric scale
            shift_num = (ord(lowerletter) + shift - 96)%26
            #letter z is 26, not 0
            if shift_num == 0:
                shift_num = 26
            # change the shift back into a letter
            new_letter = chr(shift_num + 96)
        return(new_letter)

    new_word = ''
    spacecount = 0
    # relates values in text to values in key using index
    for i in range(len(text)):
        # generates new letter in text from key using shiftletter(exclude spaces from key conversion)
        new_letter = shiftletter(key_num[(i-spacecount) % len(key_num)], text[i])
        # tracks spaces
        if new_letter == ' ':
            spacecount += 1
        new_word = new_word + new_letter
    return(new_word)


def decrypt():
    text = input('enter code: ')
    key_letter = list(input('enter key: '))

    key_num = [ord(x) - 96 for x in key_letter]

    def shift_letter(shift, letter):
        """Description: performs Caesar cypther encryption
        """
        # convert all letters to lowercase
        lower_letter = letter.lower()

        # make sure to code for the space case
        if ord(lower_letter) == 32:
            new_letter = ' '
        else:
            # change shift the number on the alphanumeric scale
            shift_num = (ord(lower_letter) - shift - 96) % 26
            # letter z is 26, not 0
            if shift_num == 0:
                shift_num = 26
            # change the shift back into a letter
            new_letter = chr(shift_num + 96)
        return (new_letter)

    new_word = ''
    space_count = 0

    # relates values in text to values in key using index
    for i in range(len(text)):
        # generates new letter in text from key using shiftletter(exclude spaces from key conversion)
        newletter = shift_letter(key_num[(i - space_count) % len(key_num)], text[i])
        # tracking spaces
        if newletter == ' ':
            space_count += 1
        new_word = new_word + newletter
    return new_word


if __name__ == "__main__":
    print(encrypt())
