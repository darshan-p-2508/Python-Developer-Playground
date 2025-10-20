# Placeholder for name substitution in the letter template
PLACEHOLDER = "[name]"

# Open the file containing names and read the contents
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Open the starting letter template and read its contents
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    # Iterate over each name in the names list
    for name in names:
        stripped_name = name.strip()  # Remove any leading/trailing whitespace from the name

        # Replace the placeholder in the letter template with the current name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Write the modified letter to a new file for the specific person
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
