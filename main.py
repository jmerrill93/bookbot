def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = 'books/frankenstein.txt'
    text = get_book_text(file_path)
    return text

def number_of_words(text):
    words = text.split()
    number = len(words)
    print(f'{number} words found in the document')

number_of_words(main())

   



    