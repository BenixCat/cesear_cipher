# Importing the art module to use the logo for the program
import art
print(art.logo)

# Defining the alphabet for the cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Taking user input for the direction, text, and shift amount for the cipher
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Function to perform the Caesar cipher encryption and decryption
def ceasar(original_text, shift_amount, direction_for_ceasar):
    # The algorithm for encoding the text
    if direction_for_ceasar == "encode":
        cipher_text = ""
        # For loop to iterate through each letter in the original text
        for letter in original_text:
            # If the letter is not in the alphabet, it is added to the cipher text as is
            if not letter in alphabet:
                cipher_text += letter
            # If the letter is in the alphabet, the shifted position is calculated and added to the cipher text
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        # Printing the encoded result
        print(f"Here is the encoded result: {cipher_text}")

    # The algorithm for decoding the text
    elif direction_for_ceasar == "decode":
        output_text = ""
        # decoding the text using a similar method as encoding
        for letter in original_text:
            # If the letter is not in the alphabet, it is added to the output text as is
            if not letter in alphabet:
                output_text += letter
            # If the letter is in the alphabet, the shifted position is calculated and added to the output text
            else:
                shifted_position = alphabet.index(letter) + (shift_amount * -1)
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        # Printing the decoded result
        print(f"Here is the decoded result: {output_text}")


# Calling the ceasar function for the first time
ceasar(original_text=text, shift_amount=shift, direction_for_ceasar=direction)
# Variable to check if the user wants to start again
is_not_over = True
# Loop to ask the user if they want to start again
# If the user types 'yes', the program will ask for the direction, text, and shift amount again
while is_not_over:
    # Asking the user if they want to start again
    want_to_start_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    # If the user types 'yes', the program will ask for the direction, text, and shift amount again
    if want_to_start_again == "yes":
        # Taking user input for the direction, text, and shift amount for the cipher again
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        # Calling the ceasar function again with the new inputs
        ceasar(text, shift, direction)
    # If the user types 'no', the program will end
    elif want_to_start_again == "no":
        is_not_over = False
        print("Goodbye!")
    # If the user types anything else, the program will print an error message
    # and ask for the input again
    # This is to ensure that the user only types 'yes' or 'no'
    else:
        print("You found me! And you also provided a invalid input. Only provide 'yes' or 'no' for this question. (Uppercase is okay.)")


