# hacked-beta-encryptodoodles

Substitution
    -Letters in code are replaced with the corresponding letters in the key (based on order)
    -Key is a 26 letters and non-repetitive
    -if key = zyxwvutsrqponmlkjihgfedcba, hi becomes rs

Caesar cipher
    -Shifts all of the letters by a certain amount of letters
    -Shift 1 will change A-->B, B-->C and so on
    -ROT13 cipher occurs when shift=13
    
Vigenere Cipher
    -Shifts by a keyword
    -If keyword was "ABCD", the encrypted message will be shifted by 1,2,3,4,1,2,3,4,etc for each letter

The One-Time Pad
    -Code letters are replaces by random letters

Enigma Machine

Playfair

AES
    -Advanced Encryption System
    -Uses exclusive OR, row shifts, and matrix multiplications to encrypt and scramble
    -User must enter a key, which is converted to a 4 by 4 matrix
    -The message is also converted to a 4 by 4 matrix
    -The message is first exclusive OR'd with the key matrix
    -Then it loops 9 times through a row shift, then a matrix multiplication by a fixed matrix, and exclusive or'd again
    -The process is reversed to decrypt


    