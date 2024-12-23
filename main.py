def get_book(file_path):
    with open(file_path) as f:
        file = f.read()
    return file
    

def word_count(text):
    n_words = text.split()
    return len(n_words)

def ch_count(text):
    new_text = text.lower()
    ch_dict = {}
    for i in new_text:
        if i in ch_dict:
            ch_dict[i] += 1
        else:
            ch_dict[i] = 1
    sorted_dict = dict(sorted(ch_dict.items()))
    
    # Remove the number and symbols
    final_dict = sorted_dict.copy()
    for i in sorted_dict:
        if i < "a":
            final_dict.pop(i)
    return final_dict



path = "books/frankenstein.txt"
book = get_book(path)
#print(book)

print("------ Begin report of", path, "------")
print("\nThere are", word_count(book), "words in the book\n")

characters = ch_count(book)
#print("\nList of character appearance in the book:")
for i in characters:
    print("The '" + i + "' character was found " + str(characters[i]) + " times")
print("\n------ End of report ------")