import json

cat = input("What is your cat's name?")

filename = 'cat.json'
with open(filename, 'w') as obj:
    json.dump(cat, obj)
    print(f"Welcome {cat}, I will remember you on your next visit!")