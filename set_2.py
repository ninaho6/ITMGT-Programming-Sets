
'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    if letter==" ":
        return " "
    
    og_position=ord(letter)-ord("A")
    new_position=(og_position+shift)%26
    new_letter=chr(new_position+ord("A"))
    
    return new_letter


def caesar_cipher(message, shift):
    def shift_letter(letter, shift):
        if letter==" ":
            return " "
        og_position=ord(letter)-ord("A")
        new_position=(og_position+shift)%26
        new_letter=chr(new_position+ord("A"))
        return new_letter

    shifted_message=""
    for letter in message:
        shifted_message += shift_letter(letter,shift)
    
    return shifted_message


def shift_by_letter(letter, letter_shift):
    if letter==" ":
        return " "
    
    og_position=ord(letter)-ord("A")
    shift=ord(letter_shift)-ord("A")
    new_position=(og_position+shift)%26
    new_letter=chr(new_position+ord("A"))
    
    return new_letter


def vigenere_cipher(message, key):
    def shift_by_letter(letter, letter_shift):
        if letter==" ":
            return " "
        og_position=ord(letter)-ord("A")
        shift=ord(letter_shift)-ord("A")
        new_position=(og_position+shift)%26
        new_letter=chr(new_position+ord("A"))
        return new_letter

    extended_key = (key * ((len(message) // len(key)) + 1))[:len(message)]
    encrypted_message = []

    key_index = 0
    for letter in message: 
        if letter == " ":
            encrypted_message.append(letter)
            key_index += 1
        else: 
            encrypted_message.append(shift_by_letter(letter, extended_key[key_index]))
            key_index += 1
    
    return ''.join(encrypted_message)


def scytale_cipher(message, shift):
    while len(message) % shift != 0: 
         message += '_'
     
    encrypted_message = ''
    for i in range(len(message)):    
        original_index = (i // shift) + (len(message) // shift) * (i % shift)
        encrypted_message += message[original_index]
    
    return encrypted_message


def scytale_decipher(message, shift):
    decrypted_message = ''
    for i in range(len(message)): 
        total_columns = len(message)//shift
        current_column = i%total_columns
        completed_row = i//total_columns
        encrypted_index = shift * current_column + completed_row 
        decrypted_message += message[encrypted_index]
    
    return decrypted_message 
