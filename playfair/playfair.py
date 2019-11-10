import string

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
        new_key_in = input("Key: ")
        validate_key(new_key_in)
        return new_key_in.lower()
    # return validated input
    return key_in.lower()


def validate_plaintext(plaintext):
    valid = True
    if len(plaintext) % 2 == 1:
        valid = False
    elif plaintext.isalpha() is False:
        valid = False
    
    if valid is False:
        print("Invalid. Try again.") # change help message later
        new_plaintext = input("Input to encrypt: ")
        validate_plaintext(new_plaintext)
        return new_plaintext
    return plaintext


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
    while count < len(plaintext) // 2:
        split_text.append(plaintext[index] + plaintext[index + 1])
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


def encrypt_same_row(two_chars, key_table):
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    encrypted_char1 = key_table[char1_index[0][0]][(char2_index[0][1] + 1) % 5]
    encrypted_char2 = key_table[char2_index[0][0]][(char1_index[0][1] + 1) % 5]
    return encrypted_char1, encrypted_char2


def encrypt_same_column(two_chars, key_table):
    transposed_table = list(zip(*key_table))
    char1_index = get_index(two_chars[0], transposed_table)
    char2_index = get_index(two_chars[1], transposed_table)
    encrypted_char1 = transposed_table[char1_index[0][1]][(char1_index[0][1] + 1) % 5]
    encrypted_char2 = transposed_table[char2_index[0][1]][(char2_index[0][1] + 1) % 5]
    return encrypted_char1, encrypted_char2


def get_index(item, key_table):
    twoD_index = [(i, row.index(item)) for i, row in enumerate(key_table) if item in row]
    return twoD_index


def encrypt_rectangle(two_chars, key_table):
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    encrypted_char1 = key_table[char1_index[0][0]][char2_index[0][1]]
    encrypted_char2 = key_table[char2_index[0][0]][char1_index[0][1]]
    return encrypted_char1, encrypted_char2


def encrypt(keyword, user_in):
    validated_key = validate_key(keyword)
    key_table = generate_key_table(validated_key)
    processed_text = split_text(user_in)

    encrypted_message = []
    for i in processed_text:
        if in_same_row(i, key_table):
            encrypted_char1, encrypted_char2 = encrypt_same_row(i, key_table)
            encrypted_message.append(encrypted_char1)
            encrypted_message.append(encrypted_char2)
        elif in_same_column(i, key_table):
            encrypted_char1, encrypted_char2 = encrypt_same_column(i, key_table)
            encrypted_message.append(encrypted_char1)
            encrypted_message.append(encrypted_char2)
        else:
            encrypted_char1, encrypted_char2 = encrypt_rectangle(i, key_table)
            encrypted_message.append(encrypted_char1)
            encrypted_message.append(encrypted_char2)
    return ''.join(encrypted_message)


def decrypt(user_in):
    pass


if __name__ == "__main__":
    key_word = input("Enter key> ")
    plaintext = input("Enter plaintext: ")
    processed_plaintext = validate_plaintext(plaintext)

    print(encrypt(key_word, processed_plaintext))
