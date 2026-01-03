import sys
from stats import get_word_count
from stats import get_char_count
from stats import sort_char_list

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    sorted_char_stats = sort_char_list(get_char_count(get_book_text(sys.argv[1])))
    #sorted_char_stats = sort_char_list(get_char_count(get_book_text("books/frankenstein.txt")))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(sys.argv[1]))} total words")
    print("--------- Character Count -------")
    for char in sorted_char_stats:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()