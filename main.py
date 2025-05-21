# main.py
from stats import number_of_words
from stats import number_of_characters
from stats import get_sorted_characters
from stats import print_report

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(file_path)
    word_count = number_of_words(text)
    character_dict = number_of_characters(text)
    sorted_characters = get_sorted_characters(character_dict)
    
    #Printing the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("---------- Character Count -------")
    print_report(sorted_characters)
    print("============= END ===============")

main()
   