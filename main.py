import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    

    else:
        path_to_file = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words(get_book_text(path_to_file))} total words")
        print("--------- Character Count -------")
        for item in sorted(get_book_text(path_to_file)):
            print(f"{item['letter']}: {item['num']}")
        print("============= END ===============")

from stats import (
    number_of_words,
    num_of_characters,
    sort_on,
    sorted
)


# from stats import num_of_characters

# from stats import sort_on

# from stats import sorted

# from stats import report

main()
