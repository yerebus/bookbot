import sys
from stats import get_num_words, get_num_chars
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1] 
        print("============ BOOKBOT ============")
        get_book_text(book)
        print("----------- Word Count ----------")
        get_num_words(book)
        print("--------- Character Count -------")
        get_num_chars(book)    
def get_book_text(book):
    with open(book) as f:
        file_content = f.read()
        print(file_content)
main()
