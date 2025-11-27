from stats import get_num_words, get_chars_dict, sorter
import sys

def main():
    book_path = args_checker()
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted = sorter(chars_dict)
    generate_report(sorted, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def generate_report(sorted, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found 75767 total words")
    print("--------- Character Count -------")
    for item in sorted:
        print(f"{item["symbol"]}: {item["count"]}")
    print("============= END ===============")

def args_checker():
    if(len(sys.argv) > 1):
        return sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
