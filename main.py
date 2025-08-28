import sys
from stats import character_count
from stats import sort_by_character_counts
from stats import word_count

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in chars_sorted_list:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py books/frankenstein.txt")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = word_count(text)
    character_dict = character_count(text)
    chars_sorted_list = sort_by_character_counts(character_dict)
    print_report(book_path, num_words, chars_sorted_list)

main()
