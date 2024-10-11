
def letter_count(text):
    lower_case = text.lower()
    letters = {}
    for i in lower_case:
        if i.isalpha():
            if i not in letters:
                letters[i] = 0
            letters[i] += 1
    return letters

def sort(dict):
    return dict["count"]

with open ("books/frankenstein.txt") as f:
    file_contents = f.read()

char_count = letter_count(file_contents)
word_count = len(file_contents.split())

char_list = [{"char": char, "count": count} for char, count in char_count.items()]
char_list.sort(reverse=True, key=sort)


print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words are found in the document")
print()
for char_dict in char_list:
    print(f"The {char_dict["char"]} character was found {char_dict["count"]} times")
print("--- End report ---")