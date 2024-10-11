
def letter_count(text):
    lower_case = text.lower()
    letters = {}
    for i in lower_case:
        if i.isalpha():
            if i not in letters:
                letters[i] = 0
            letters[i] += 1
    return letters

with open ("books/frankenstein.txt") as f:
    file_contents = f.read()

char_count = letter_count(file_contents)
word_count = len(file_contents.split())

print(f"Word count is: {word_count}")
print(char_count)