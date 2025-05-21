# stats.py
def number_of_words(text):
    words = text.split()
    number = len(words)
    return number

def number_of_characters(text):

    character_dict = {}
    # Convert the text to lowercase to count characters case-insensitively
    lower_case_characters = text.lower()
    for character in lower_case_characters:
        if character.isalpha():
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
    return character_dict

def get_sorted_characters(character_dict):
    # Only sort, don't print
    sorted_characters = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters

def print_report(sorted_characters):
    # Print only alphabetic characters or specific format
    for char, count in sorted_characters:
        if char.isalpha():  # Only print alphabet letters
            print(f'{char}: {count}')

