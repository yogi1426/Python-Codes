import json
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm

data = json.load(open("data.json"))
query = input("Enter a word to Search : ")
#sm(None,"rainn","rain")) #compares the similarity ratio
data_key = list(data.keys())

def translate(query):
    query = query.lower()
    if (query in data.keys()):
        a = data[query]
        for i in a:
            print(i)
    elif(gcm(query,data_key,3)):
        query = gcm(query,data_key,3)[0]
        ans = input("Did you mean  - '%s'? " %query)
        if (ans == 'yes'):
            translate(query)
        elif (ans == "no"):
            print("Sorry, No Result")
        else:
            print("Sorry, Did not get your entry.")
    else:
        print("Sorry, No Result")

translate(query)




