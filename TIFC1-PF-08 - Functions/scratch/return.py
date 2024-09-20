def describe_pet(pet_name, animal_type):
    pet_info = pet_name + ", " + animal_type
    return pet_info

my_pet = describe_pet('scout', 'dachshund')
print(my_pet)