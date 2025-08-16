def number_of_words(file_contents):
    counter = 0
    words = file_contents.split()
    for word in words:
        counter += 1
    num_words = counter
    return num_words

def num_of_characters(file_contents):
    test = file_contents.lower()
    characters = [x for x in test]
    characters_dict = {}
    for character in characters:
        if character not in characters_dict:
            characters_dict[f"{character}"] = 1
        else:
            characters_dict[character] += 1
    return characters_dict

def sort_on(items):
    return items["num"]

def sorted(file_contents):
    list = []
    dict_of_letters = num_of_characters(file_contents)
    
    for letter in dict_of_letters:
        if letter.isalpha() == True:
            list.append({"letter": letter, "num": dict_of_letters[letter]})

    list.sort(reverse=True, key=sort_on)
    return list

def report(file_contents):
    for item in sorted(file_contents):
        print(f"{item['letter']}: {item['num']}")

