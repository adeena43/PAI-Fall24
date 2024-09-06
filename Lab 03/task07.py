def replace_mistake(word_with_mistake, incorrect_letter, correct_letter):
    try:
        # Read the file content
        with open('replacement_needed.txt', 'r') as file:
            content = file.read()
        
        # Ask user for input
        #word_with_mistake = input("Enter the word which contains the wrong letter: ").strip()
        #incorrect_letter = input("Enter the letter to be replaced: ").strip()
        #correct_letter = input("Enter the correct letter to replace with: ").strip()
        
        # Basic validation
        if not word_with_mistake or not incorrect_letter or not correct_letter:
            print("All input fields must be filled.")
            return
        
        # Replace the incorrect letter in the word
        if incorrect_letter in word_with_mistake:
            modified_word = word_with_mistake.replace(incorrect_letter, correct_letter)
        else:
            print(f"The letter '{incorrect_letter}' is not in the word '{word_with_mistake}'.")
            return
        
        # Replace the word with the modified word in the content
        updated_content = content.replace(word_with_mistake, modified_word)
        
        # Write the updated content back to the file
        with open('replacement_needed.txt', 'a') as file:  # Open file in append mode
          
            file.write("\n\nUpdated Content:\n")
            file.write(updated_content)
        
        print("Updated the file successfully!")

    except FileNotFoundError:
        print("The file 'replacement_needed.txt' was not found.")
    except PermissionError:
        print("Permission denied: Cannot read/write the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
replace_mistake("art", "t", "e")
