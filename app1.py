import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Do you mean %s instead ,if yes enter 'Y' other enter 'N' :" %get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return "Word doesn't exist. Please double check it"
        else:
            return "we don't understand your query"
    else:
        return "Word doesn't exist.Please double check it."

word=input("Enter word: ")

output=translate(word);
if type(output) == list:
    for item in output:
        print(item)
else: print(output)


