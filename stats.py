def word_count(book_text):
    num_words = book_text.split()
    return len(num_words)

def character_count(book_text):
    character_dict = {}

    for characters in book_text.lower():
        if characters in character_dict:
            character_dict[characters] += 1
        elif characters not in character_dict:
            character_dict[characters] = 1

    return character_dict

def sort_on(items):
    return items["num"]
    
def sort_by_character_counts(dictionary):
    sorted_list = []

    for char, count in dictionary.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


    



