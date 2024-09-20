def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='dachshund', pet_name='scout')
describe_pet(pet_name='scout', animal_type='dachshund')