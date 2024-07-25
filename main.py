def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    letter_count = count_chars(text)
    sortable_letter_count = kvp_list(letter_count)
    # sortable_letter_count.sort(reverse=True, key=sort_on)
    print(sortable_letter_count)
    sortable_letter_count.sort(reverse=True, key=sort_on)
    print(sortable_letter_count)


def word_count(text):
    words = text.split() 
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_chars(text):
    text = text.lower()
    abc_dict = {}
    for alpha in text:
        if alpha.isalpha() == True:
            if alpha not in abc_dict:
                abc_dict[alpha] = 1
            else:
                abc_dict[alpha] += 1
    return abc_dict

def kvp_list(dict): # rename this function. Return only list dict.
    list_dict = []
    for letter in dict:
        new_dict = {}
        count = dict[letter]
        new_dict[letter] = count
        list_dict.append(new_dict)
    return list_dict

def sort_on(dict):
    return dict['count']

main()
