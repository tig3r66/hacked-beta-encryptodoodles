# hacked-beta-encryptodoodles
The following encryption ciphers were created during the hacked-beta 2019 competition.
The main file (Main.py) incorporates Caesar, Viginere, Enigma, and Playfair into an encryption library that the user may select from.
A simple GUI is also provided with the encryptions above (MainTkinter.py). Substitution, The One-Time Pad, and AES are excluded from these files,
however are functional and can be located in their respective files. For future iterations, they will be 
incorporated into the main files and GUI.

Substitution
    -Letters in code are replaced with the corresponding letters in the key (based on index)
    -Key is a 26 letters and non-repetitive
    -if key = zyxwvutsrqponmlkjihgfedcba, hi becomes rs
    
Caesar cipher
    -Shifts all of the letters by a certain amount of letters
    -Shift 1 will change A-->B, B-->C and so on
    -ROT13 cipher occurs when shift=13
    
Vigenere Cipher
    -Shifts by a letter in the keyword per letter in the code
    -Each letter in the encrypted message will be shifted by the letter with the same index in the code
    -Cipher algorithm accounts for the cases that the keyword and the code are different lengths
    -For example, the code "abcd" with the key "abc" will shift the code: a by 1 letter, b by 2 letters, c by 3 letters,
    and d by one letter
     
The One-Time Pad
    -User inputted code letters are shifted alphabetically using values from 0 to 25 in a pseudorandomly generated key 
    the same length as the code
    -Most secure encryption in this package, as there is a different key for every code input
    -No predictable method for guessing the key

Enigma Machine
    -Polyalphabetic substitution cipher modeled after the Enigma machines
    -Algorithm involves a pseudo random key sequence that simulates rotor cipher machines
    -Utilizes initial positions of all 3 simulated rotors for encryption and decryption
    -Shifts the code using a modular function
    
Playfair
    -diagraph algorithm that retrieves the consequent letter
    -the "key" is a 5x5 array in which a keyword consisting of unique letters are appended in the order
    they appear, and then the rest of the alphabet is appending to the 5x5 array. If the letter is 'j',
    then 'l' is substituted.
    -letters in the input string are split into pairs of two. If the length of the string (without whitespace)
    is odd, the letter q is appended to the end of the string.
    -There are 3 cases to encrypt the message. If both letters are in the same column, take the letter directly
    below each one, wrapping around to the top of the column if the value is already at the bottom. If
    both characters are in the same row, take the letter directly to the right of the letters, wrapping
    around to the leftmost side if the letter is at the rightmost side. Finally, if neither mentioned cases are
    true, then draw the tightest fitting rectangle around the two letters, and the encoded letters are the
    letters in the corner of the 5x5 array directly opposite to the character per row.
    -To decrypt, reverse the encryption algorithm.    
    

AES
    -Advanced Encryption System
    -Uses exclusive OR, row shifts, and matrix multiplications to encrypt and scramble
    -User must enter a key, which is converted to a 4 by 4 matrix
    -The message is also converted to a 4 by 4 matrix
    -The message is first exclusive OR'd with the key matrix
    -Then it loops 9 times through a row shift, then a matrix multiplication by a fixed matrix, and exclusive or'd again
    -The process is reversed to decrypt

