import stats
import sys

# función para obtener el contenido de un libro
def get_book_text(filepath: str):
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    textContent = get_book_text(sys.argv[1])

    print("Analyzing book found at books/frankenstein.txt...")

    words = stats.count_words(textContent)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    chars = stats.count_chars_and_spaces(textContent)
    chars_list: dict[str, int] = stats.list_of_chars(chars)
    for item in chars_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()