"""Dictionary running through command prompt that returns meaning of word , understands both uppercase and lowercase and
tries to correct error in word as much as possible """

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data :
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter y if yes or n if no "  % get_close_matches(word,data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == 'n':
            return "The word does not exist."
        else :
            return "We cannot understand your entry."
    else :
        return "Word not found."


word = input("Enter the word: ")

result = translate(word)

if type(result) == list:
    for item in result:
        print(item)
else:
        print(result)
