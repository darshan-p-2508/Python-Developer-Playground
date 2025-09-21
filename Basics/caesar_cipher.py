alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# def encrypt(original_text, shift_amount):
#    ciphered_text = ""
#    for letter in original_text:
#        shifted_position = alphabet.index(letter) + shift_amount
#        ciphered_text += alphabet[shifted_position % len(alphabet)] # to handle the shift from 'z' error
#
#    print(f"Here is the encoded result: {ciphered_text}")

# def decrypt(encoded_text, shift_amount):
#    deciphered_text = ""
#    for letter in encoded_text:
#        shifted_position = alphabet.index(letter) - shift_amount
#        deciphered_text += alphabet[shifted_position % len(alphabet)]
#
#    print(f"Here is the decoded result: {deciphered_text}")

#combining the encrypt and decrypt function to one caesar

def caesar(original_text, shift_amount, encode_or_decode):
    cryptic_text = ""
    if encode_or_decode.lower() == "decode":
                shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cryptic_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cryptic_text += alphabet[shifted_position] # to handle the shift from 'z' error

    print(f"Here is the {encode_or_decode}d result: {cryptic_text}")
        
should_continue = True

while should_continue:
    
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt the message:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    
    to_continue = input("Would you like to continue? Type 'Yes' or 'No':\n")
    if to_continue.lower() == "no":
        should_continue = False
        print("Goodbye")
