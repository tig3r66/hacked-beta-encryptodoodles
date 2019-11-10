import string

def validate_key(key_in):
    """Description: Validates a potential key from user input to use in the
    playfair cipher.
    """
    valid = True
    key_list = ''.join([i for i in key_in if i in string.ascii_lowercase])
    if key_list.isalpha() is False:
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
    return key_list.lower()


def validate_plaintext(plaintext):
    valid = True
    plain_list = ''.join([i for i in plaintext if i in string.ascii_lowercase])

    if len(plain_list) % 2 == 1:
        valid = False
    elif plain_list.isalpha() is False:
        valid = False

    if valid is False:
        print("Invalid. Try again.") # change help message later
        new_plaintext = input("Input to encrypt: ")
        new_plain_list = [i for i in new_plaintext if i in string.ascii_lowercase]
        validate_plaintext(new_plain_list)
        return ''.join(new_plain_list)
    return ''.join(plain_list)


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


def get_index(item, key_table):
    twoD_index = [(i, row.index(item)) for i, row in enumerate(key_table) if item in row]
    return twoD_index


def encrypt_same_row(two_chars, key_table):
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    encrypted_char1 = key_table[char1_index[0][0]][(char1_index[0][1] + 1) % 5]
    encrypted_char2 = key_table[char2_index[0][0]][(char2_index[0][1] + 1) % 5]
    return encrypted_char1, encrypted_char2


def encrypt_same_column(two_chars, key_table):
    transposed_table = list(zip(*key_table))
    char1_index = get_index(two_chars[0], transposed_table)
    char2_index = get_index(two_chars[1], transposed_table)
    encrypted_char1 = transposed_table[char1_index[0][0]][(char1_index[0][1] + 1) % 5]
    encrypted_char2 = transposed_table[char2_index[0][0]][(char2_index[0][1] + 1) % 5]
    return encrypted_char1, encrypted_char2


def encrypt_rectangle(two_chars, key_table):
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    encrypted_char1 = key_table[char1_index[0][0]][char2_index[0][1]]
    encrypted_char2 = key_table[char2_index[0][0]][char1_index[0][1]]
    return encrypted_char1, encrypted_char2


def encrypt(keyword, user_in):
    validated_key = validate_key(keyword)
    key_table = generate_key_table(validated_key)
    processed_text = validate_plaintext(user_in)
    good_processed_text = split_text(processed_text)

    encrypted_message = []
    for i in good_processed_text:
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


def decrypt_same_row(two_chars, key_table):
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    decrypted_char1 = key_table[char1_index[0][0]][char1_index[0][1] - 1]
    decrypted_char2 = key_table[char2_index[0][0]][char2_index[0][1] - 1]
    return decrypted_char1, decrypted_char2


def decrypt_same_column(two_chars, key_table):
    transposed_table = list(zip(*key_table))
    char1_index = get_index(two_chars[0], transposed_table)
    char2_index = get_index(two_chars[1], transposed_table)
    decrypted_char1 = transposed_table[char1_index[0][0]][char1_index[0][1] - 1]
    decrypted_char2 = transposed_table[char2_index[0][0]][char2_index[0][1] - 1]
    return decrypted_char1, decrypted_char2


def decrypt_rectangle(two_chars, key_table):
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    decrypted_char1 = key_table[char1_index[0][0]][char2_index[0][1]]
    decrypted_char2 = key_table[char2_index[0][0]][char1_index[0][1]]
    return decrypted_char1, decrypted_char2


def decrypt(keyword, user_in):
    validated_key = validate_key(keyword)
    key_table = generate_key_table(validated_key)
    processed_text = validate_plaintext(user_in)
    good_processed_text = split_text(processed_text)

    decrypted_message = []
    for i in good_processed_text:
        if in_same_row(i, key_table):
            decrypted_char1, decrypted_char2 = decrypt_same_row(i, key_table)
            decrypted_message.append(decrypted_char1)
            decrypted_message.append(decrypted_char2)
        elif in_same_column(i, key_table):
            decrypted_char1, decrypted_char2 = decrypt_same_column(i, key_table)
            decrypted_message.append(decrypted_char1)
            decrypted_message.append(decrypted_char2)
        else:
            decrypted_char1, decrypted_char2 = decrypt_rectangle(i, key_table)
            decrypted_message.append(decrypted_char1)
            decrypted_message.append(decrypted_char2)
    return ''.join(decrypted_message)


if __name__ == "__main__":
    # key_word = input("Enter key> ")
    # encrypted_text = input("Enter encrypted text: ")
    # print(decrypt(key_word, encrypted_text))

    key_word = input("Enter key> ")
    plaintext = input("Enter plaintext: ")
    print(encrypt(key_word, plaintext))
    