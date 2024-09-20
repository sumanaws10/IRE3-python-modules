def describe_pet(pet_name, animal_type, pet_last_name=' '):
    if pet_last_name:
        pet_info = pet_name + ', ' + pet_last_name + ', ' + animal_type
    else:
        pet_info = pet_name + ', ' + animal_type
    return pet_info

my_pet = describe_pet('Frankie', 'dachshund')
print(my_pet)

my_pet = describe_pet('Frankie', 'dachshund', 'Furter')
print(my_pet)