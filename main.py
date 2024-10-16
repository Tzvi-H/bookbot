def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = word_count(file_contents)
        characters = character_count(file_contents)
        sorted_counts = something(characters)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print()
        for item in sorted_counts:
            k = list(item.keys())[0]
            v = list(item.values())[0]
            print(f"The '{k}' character was found {v} times")
        print("--- End report ---")

def word_count(text):
    lines = text.split()
    return len(lines)

def character_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def something(char_count):
    result = []
    for k,v in char_count.items():
        if k.isalpha():
            result.append({k: v})
    result.sort(reverse=True, key=lambda x: list(x.values())[0])
    return result

main()