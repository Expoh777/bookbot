def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_counts = count_characters(text)
    sorted_characters = sort_character_counts(character_counts)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for character in sorted_characters:
        print(f"The '{character["char"]}' character was found {character["num"]} times")
    print("--- End Report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)
    
def count_characters(text):
    letter_dict = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def sort_character_counts(character_counts):
    char_sorted = []
    for char in character_counts:
        if char.isalpha() == True:
            char_sorted.append({"char": char, "num": character_counts[char]})
    char_sorted.sort(reverse = True, key = sort_on)
    return char_sorted

main()