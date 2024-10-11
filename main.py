letters = {"abcdefghijklmnopqrstuvwxyz"}
with open ("books/frankenstein.txt") as f:
    file_contents = f.read()

def word_counting():
    words = file_contents.split()
    word_count = words.__len__()

#def letter_count():
    #lower_case = file_contents.lower()
    #count_letters = lower_case.__len__(letters)

    #print(count_letters)
def main():
    return word_counting