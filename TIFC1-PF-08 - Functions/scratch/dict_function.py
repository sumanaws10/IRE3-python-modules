def describe_pet(pet_first_name, pet_last_name):
    my_pet = {'first': pet_first_name, 'last': pet_last_name}       # has 2 parameter, create dict.
    return my_pet
# above function create dictonary
dog = describe_pet('Frankie', 'Furter')
print(dog)

for x in dog.values():
    print(x)
#for key, value in dog.items():
 #   print(value)
for key in dog.keys():
    print(key)