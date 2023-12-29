with open("./books/frankenstein.txt") as f:
    frankenstein = f.read()

def word_counter(text):
    words = text.split()
    return len(words)

def letter_counter(text):
    _dict = {}
    text = text.lower()
    txt = text.replace("\n", "")
    txt = text.replace(" ", "")

    for i in txt:
        keys = _dict.keys()
        if i in keys:
            _dict[i] += 1
        else:
            _dict[i] = 1
            
    return _dict

def documentation(word_count, letter_dict):
    keys = []
    values = []
    t_dict = {}

    for i in letter_dict:
        if i.isalpha():
            keys.append(i) 
            values.append(letter_dict[i])

    print(f"--- Begin report of books/{f} ---")
    print(f"{word_count} words found in the document")

    for i in range(len(keys)):
        print(f"The '{keys[i]}' character was found {values[i]} times")

    print("--- End report ---")

x = word_counter(frankenstein)
y = letter_counter(frankenstein)

documentation(x, y)