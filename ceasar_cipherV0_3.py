# Importing the art module to use the logo for the program
import art
print(art.logo)

# Defining the alphabet for the cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Defining the ceasar function to encode or decode the text based on user input
def ceasar(original_text, shift_amount, direction_for_ceasar):
    result_text = ""
    # Adjusting the shift amount based on whether we are encoding or decoding
    # If decoding, we negate the shift amount to reverse the encoding process
    # If encoding, we keep the shift amount as is to shift forward in the alphabet
    shift_amount *= -1 if direction_for_ceasar == "decode" else 1

    # Iterating through each letter in the original text
    for letter in original_text:
        # If the letter is not in the alphabet, we add it to the result text as is
        if letter not in alphabet:
            result_text += letter
        # If the letter is in the alphabet, we find its index and apply the shift
        else:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            result_text += alphabet[shifted_position]
    # Printing the result based on whether we are encoding or decoding
    print(f"Here is the {'decoded' if direction_for_ceasar == 'decode' else 'encoded'} result: {result_text}")

# Main program loop to get user input and call the ceasar function
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Calling the ceasar function for the first time with user inputs
ceasar(original_text=text, shift_amount=shift, direction_for_ceasar=direction)

# Loop to ask the user if they want to run the program again
while True:
    # Asking the user if they want to run the program again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    # If the user wants to run the program again, we get new inputs and call the ceasar function again
    if restart == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        ceasar(text, shift, direction)
    # If the user does not want to run the program again, we break out of the loop and end the program
    elif restart == "no":
        break
    # In the case of invalid input, we print a message to the user
    # and ask them to provide a valid input
    # This for ensures that the program does not crash if the user provides an invalid input and the user only types 'yes' or 'no'
    else:
        print("You found me! And you also provided a invalid input. Only provide 'yes' or 'no' for this question. (Uppercase is okay.)")

# In version 0.3, I shortened the code with Chatgpt's help by removing the redundant code to make the code better.