import string
import math

def validate_key(key_in):
    """Description: Validates a potential key from user input to use in the
    playfair cipher.
    """
    valid = True
    # validation cases
    if key_in.isalpha() is False:
        valid = False
    else:
        char_dict = dict()
        for i in key_in:
            if i not in char_dict:
                char_dict[i] = 1
            else:
                valid = False
                break

    if valid is False:
        print("Invalid. Try again.") # change help message later
        new_key_in = input("Input to encrypt: ")
        validate_key(new_key_in)
        return new_key_in.lower()
    # return validated input
    return key_in.lower()


def generate_key_table(validated_key):
    """Description: returns a 5x5 array according to the playfair cipher.
    """
    key_square = [[], [], [], [], []]

    outer_index, count = 0, 0
    # updating key_square with validated_key
    for i in validated_key:
        if count < 5:
            key_square[outer_index].append(i)
        else:
            count = 0
            outer_index += 1
            key_square[outer_index].append(i)
        count += 1

    # filling rest of key_square
    ascii_index = 0
    for i in range(26):
        if ((string.ascii_lowercase[ascii_index] in validated_key) or (ascii_index == 9)):
            ascii_index += 1
            continue
        elif count < 5:
            key_square[outer_index].append(string.ascii_lowercase[ascii_index])
        else:
            count = 0
            outer_index += 1
            key_square[outer_index].append(string.ascii_lowercase[ascii_index])
        ascii_index += 1
        count += 1

    return key_square


def split_text(plaintext):
    """Description: takes plaintext and splits them into a list of 2
    characters.
    """
    # removing spaces
    plaintext = ''.join(plaintext.split())
    split_text = []
    count, index = 0, 0
    while count < math.ceil(len(plaintext) / 2):
        try:
            split_text.append(plaintext[index] + plaintext[index + 1])
        except IndexError:
            split_text.append(plaintext[index])
        count += 1
        index += 2

    return split_text


def in_same_row(two_chars, key_table):
    for i in range(len(key_table)):
        if (two_chars[0] in key_table[i]) and (two_chars[1] in key_table[i]):
            return True
    return False


def in_same_column(two_chars, key_table):
    transposed_table = list(zip(*key_table))
    for i in range(len(transposed_table)):
        if (two_chars[0] in transposed_table[i]) and (two_chars[1] in transposed_table[i]):
            return True
    return False


def encode_same_row(two_chars, key_table):
    pass


def encrypt(keyword, user_in):
    validated_key = validate_key(keyword)
    key_table = generate_key_table(validated_key)
    processed_text = split_text(user_in)

    encrypted_message = []

    for i in processed_text:
        if in_same_row(i, key_table):
            pass
        elif in_same_column(i, key_table):
            pass
        else:
            pass

    return ''.join(encrypted_message)


def decrypt(user_in):
    pass


if __name__ == "__main__":
    key_word = input("Enter key> ")
    plaintext = input("Enter plaintext: ")

    print(encrypt(key_word, plaintext))
