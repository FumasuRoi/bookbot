def get_word_count(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    book_text_lower = book_text.lower()
    results = {}
    for char in book_text_lower:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1
    return results

def sort_on(items):
    return items["num"]

def sort_char_list(char_dict):
    sorted_list = []
    for char in char_dict:
        single_dict = {"char": char, "num": char_dict[char]}
        sorted_list.append(single_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

