#Use a dictionary to store information about a person you know. Store their first name, last name, age, 
# and the city in which they live. You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

Person = {
    'name': 'Pryanka',
    'last_name' : 'Roy',
    'age' : '20',
    'city' : 'Dublin'}
print(Person['name'])
print(Person['last_name'])  # access key value pair
print(Person['age'])
print(Person['city'])
print(Person)

#Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your
#  dictionary. Think of a favorite number for each person, and store each as a value in your dictionary.
#  Print each person’s name and their favorite number. For even more fun, poll a few friends and get some
#  actual data for your program.

Persons = {
    'Person1' : { 
        'Name': 'Ruhi',
        'Favorite_number': '10',
        },
    'Person2' : { 
        'Name': 'Viaan',
        'Favorite_number': '20',
        },
    'Person3' : { 
        'Name': 'Sushil',
        'Favorite_number': '30',
        },
    'Person4' : { 
        'Name': 'Dishu',
        'Favorite_number': '40',
        },
    'Person5' : { 
        'Name': 'Aatiya',
        'Favorite_number': '50',
        }
}
for Person_number, Person_info in Persons.items():
    print(Person_number)
    print(Person_info)

########################
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary
Rivers = {
    'Nile': 'Egypt',
    'Ganga': 'Bihar',
    'Yamuna': 'Haryana'
}

for key, value in Rivers.items():
    print(f"The key is {key} and the value is {value}")

