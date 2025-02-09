def read_file(filepath):
    with open(filepath, "r") as book:
        return book.read()


def count_words(text):
    return len(text.split())


def count_chars(text):
    char_dict = dict()
    for char in text:
        char = char.lower()
        if char not in char_dict.keys():
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def print_results(filepath, wordcount, character_dict):
    print(f"--- Begin report of {filepath} ---")
    print(f"{wordcount} words found in the document\n")
    for char in character_dict.keys():
        if char.isalpha():
            print(f"The '{char}' was found {character_dict[char]} times")


if __name__ == "__main__":
    filepath = "books/Frankenstein.txt"
    text = read_file(filepath)
    word_count = count_words(text)
    char_dict = count_chars(text)
    print_results(filepath, word_count, char_dict)
