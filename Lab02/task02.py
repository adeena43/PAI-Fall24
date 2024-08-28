word = input("Enter a word: ")
if(word.endswith('a') or word.endswith('e') or word.endswith('i') or word.endswith('o') or word.endswith('u') or word.endswith('A') or word.endswith('E') or word.endswith('I') or word.endswith('O') or word.endswith('U')):
    print(f"{word} ends with a vowel")

else:
    print(f"{word} ends with a consonant")
