# Implements the playfair encryption algorithm. Requires the string module to
# be imported.

def validate_key(key_in):
    """Description: Validates a potential key from user input to use in the
    playfair cipher. For a given input key, if there are invalid characters,
    those characters are removed and the string is rejoined. Valid characters
    consist of unique ASCII letters.

    Arguments:
        key_in (string): keyword to use for the playfair cipher.
    Returns:
        key_list (string): if key_in is a valid keyword, return a lowercase
        version of the input.
    """
    key_list = ''.join([i for i in key_in if i in string.ascii_letters])
    valid = True
    if key_list.isalpha() is False:
        valid = False
    else:
        char_dict = dict()
        for i in key_in:
            if i not in char_dict:
                char_dict[i] = 1
            else:
                print("The input contains duplicate letters. Choose a keyword"
                     " that contains unique letters.")
                valid = False
                break

    if valid is False:
        new_key_in = input("Key: ")
        validate_key(new_key_in)
        return new_key_in.lower()
    return key_list.lower()


def validate_plaintext(plaintext):
    """Desscription: validates plaintext input from user input to use in the
    playfair cipher. For the given input, if there are inavlid characters,
    those characters are removed and the string is rejoined. Valid characters
    consist of ASCII letters (repeats are permitted). If the length of
    plaintext is odd, the letter 'q' is appended to the end of the word.

    Arguments:
        plaintext (string): string used to either encode or decode.
    Returns:
        plain_list (string): if plaintext is a valid string, return a
        lowercase version of the input.
    """
    valid = True
    plain_list = ''.join([i for i in plaintext if i in string.ascii_letters])

    if len(plain_list) % 2 == 1:
        plain_list += 'q'
    elif plain_list.isalpha() is False:
        valid = False

    if valid is False:
        print("Invalid. Try again.") # change help message later
        new_plaintext = input("Input to encrypt: ")
        new_plain_list = [i for i in new_plaintext if i in string.ascii_letters]
        validate_plaintext(new_plain_list)
        return ''.join(new_plain_list)
    return plain_list.lower()


def get_space_indices(plaintext):
    """Description: for a given string input, returns a list containing the
    indices in which spaces occur.

    Arguments:
        plaintext (string): string used to either encode or decode.
    Returns:
        space_indices (list): list contains all indices in which spaces occur.
    """
    space_indices = []
    count = 0
    for i in plaintext:
        if i == ' ':
            space_indices.append(count)
        count += 1
    return space_indices


def generate_key_table(validated_key):
    """Description: returns a 5x5 array containing characters according to the
    playfair cipher. In particular, J is replaced with L, and each of the
    characters in the 5x5 array is unique.

    Arguments:
        validated_key (string): takes a valid key as input.
    Returns:
        key_square (array): 5x5 array containing characters according to the
        playfair cipher.
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

    Arguments:
        plaintext (string): string used to either encode or decode.
    Returns:
        split_text (list): list containing a valid input string in which the
        string is broken into substrings of length 2, with the first break
        point starting at index = 1.
    """
    split_text = []
    count, index = 0, 0
    while count < len(plaintext) // 2:
        split_text.append(plaintext[index] + plaintext[index + 1])
        count += 1
        index += 2
    return split_text


def in_same_row(two_chars, key_table):
    """Description: returns True if the character pair is in the same row of
    the 5x5 matrix. Else, returns False.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        bool: if the two characters are in the same row, return True. Else,
        return False.
    """
    for i in range(len(key_table)):
        if (two_chars[0] in key_table[i]) and (two_chars[1] in key_table[i]):
            return True
    return False


def in_same_column(two_chars, key_table):
    """Description: returns True if the character pair is in the same column
    of the 5x5 matrix. Else, returns False.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        bool: if the two characters are in the same column, return True. Else,
        return False.
    """
    # applying a transposition to the 5x5 array
    transposed_table = list(zip(*key_table))
    for i in range(len(transposed_table)):
        if ((two_chars[0] in transposed_table[i])
            and (two_chars[1] in transposed_table[i])):
                return True
    return False


def get_index(item, key_table):
    """Description: returns the index of an item of interest in a 2D array.

    Arguments:
        item: item of interest.
        key_table (list): a 2D array to find the item of interest.
    Returns:
        twoD_index (list): a list containing tuples at the first instance for
        every row at which the item of interest is found.
    """
    twoD_index = [(i, row.index(item)) for i, row in enumerate(key_table) if item in row]
    return twoD_index


def encrypt_same_row(two_chars, key_table):
    """Description: given that the two characters are in the same row, encrypt
    the two characters by taking the letter in key_table to the index to the
    right of that letter. If the letter is already at the rightmost character,
    wrap around the table and take the leftmost character.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        encrypted_char1 (string): encrypted version of the first character in
        two_chars.
        encrypted_char2(string): encrypted version of the second character in
        two_chars.
    """
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    encrypted_char1 = key_table[char1_index[0][0]][(char1_index[0][1] + 1) % 5]
    encrypted_char2 = key_table[char2_index[0][0]][(char2_index[0][1] + 1) % 5]
    return encrypted_char1, encrypted_char2


def encrypt_same_column(two_chars, key_table):
    """Description: given that the two characters are in the same column,
    encrypt the two characters by taking the letter in key_table to the bottom
    of that letter. If the letter is already at the lowermost character, wrap
    around the table and take the upmost character.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        encrypted_char1 (string): encrypted version of the first character in
        two_chars.
        encrypted_char2(string): encrypted version of the second character in
        two_chars.
    """
    transposed_table = list(zip(*key_table))
    char1_index = get_index(two_chars[0], transposed_table)
    char2_index = get_index(two_chars[1], transposed_table)
    encrypted_char1 = transposed_table[char1_index[0][0]][(char1_index[0][1] + 1) % 5]
    encrypted_char2 = transposed_table[char2_index[0][0]][(char2_index[0][1] + 1) % 5]
    return encrypted_char1, encrypted_char2


def encrypt_rectangle(two_chars, key_table):
    """Description: given that the two characters are neither in the same row
    or same column, take the two characters as the corners of a rectangle in
    which the characters are the rightmost or leftmost and bottommost or
    topmost characters. Encrypt the two characters by taking the character in
    the corner directly opposite to the characters of interest.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        encrypted_char1 (string): encrypted version of the first character in
        two_chars.
        encrypted_char2(string): encrypted version of the second character in
        two_chars.
    """
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    encrypted_char1 = key_table[char1_index[0][0]][char2_index[0][1]]
    encrypted_char2 = key_table[char2_index[0][0]][char1_index[0][1]]
    return encrypted_char1, encrypted_char2


def encrypt(keyword, user_in):
    """Description: encrypt the user input according to the playfair cipher
    algorithm.

    Arguments:
        keyword (string): a keyword (will be validated). If not valid, the
        user will be promped to enter a new keyword.
        user_in (string): user input to encrypt (note that user_in is
        validated in this function).
    Returns:
        encrypted_message (string): the encrypted message.
    """
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
    """Description: given that the two characters are in the same row, decrypt
    the two characters by taking the letter in key_table to the index to the
    left of that letter. If the letter is already at the leftmost character,
    wrap around the table and take the rightmost character.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        encrypted_char1 (string): encrypted version of the first character in
        two_chars.
        encrypted_char2(string): encrypted version of the second character in
        two_chars.
    """
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    decrypted_char1 = key_table[char1_index[0][0]][char1_index[0][1] - 1]
    decrypted_char2 = key_table[char2_index[0][0]][char2_index[0][1] - 1]
    return decrypted_char1, decrypted_char2


def decrypt_same_column(two_chars, key_table):
    """Description: given that the two characters are in the same column,
    decrypt the two characters by taking the letter in key_table to the top of
    that letter. If the letter is already at the uppermost character, wrap
    around the table and take the lowermost character.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        encrypted_char1 (string): encrypted version of the first character in
        two_chars.
        encrypted_char2(string): encrypted version of the second character in
        two_chars.
    """
    transposed_table = list(zip(*key_table))
    char1_index = get_index(two_chars[0], transposed_table)
    char2_index = get_index(two_chars[1], transposed_table)
    decrypted_char1 = transposed_table[char1_index[0][0]][char1_index[0][1] - 1]
    decrypted_char2 = transposed_table[char2_index[0][0]][char2_index[0][1] - 1]
    return decrypted_char1, decrypted_char2


def decrypt_rectangle(two_chars, key_table):
    """Description: given that the two characters are neither in the same row
    or same column, take the two characters as the corners of a rectangle in
    which the characters are the rightmost or leftmost and bottommost or
    topmost characters. Decrypt the two characters by taking the character in
    the corner directly opposite to the characters of interest.

    Arguments:
        two_chars (string): a valid string of length 2.
        key_table (array): a valid playfair array (5x5).
    Returns:
        encrypted_char1 (string): encrypted version of the first character in
        two_chars.
        encrypted_char2(string): encrypted version of the second character in
        two_chars.
    """
    char1_index = get_index(two_chars[0], key_table)
    char2_index = get_index(two_chars[1], key_table)
    decrypted_char1 = key_table[char1_index[0][0]][char2_index[0][1]]
    decrypted_char2 = key_table[char2_index[0][0]][char1_index[0][1]]
    return decrypted_char1, decrypted_char2


def decrypt(keyword, user_in):
    """Description: decrypt the user input according to the playfair cipher
    algorithm.

    Arguments:
        keyword (string): a keyword (will be validated). If not valid, the
        user will be promped to enter a new keyword.
        user_in (string): user input to encrypt (note that user_in is
        validated in this function).
    Returns:
        encrypted_message (string): the encrypted message.
    """
    validated_key = validate_key(keyword)
    key_table = generate_key_table(validated_key)
    processed_text = validate_plaintext(user_in)
    # indices = get_space_indices(user_in)
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
    # for i in indices:
    #     decrypted_message.insert(i, ' ')
    return ''.join(decrypted_message)


if __name__ == "__main__":
    import string

    # key_word = input("Enter key> ")
    # encrypted_text = input("Enter encrypted text: ")
    # print(decrypt(key_word, encrypted_text))

    key_word = input("Enter key> ")
    plaintext = input("Enter plaintext: ")
    print(encrypt(key_word, plaintext))
