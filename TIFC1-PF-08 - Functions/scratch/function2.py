def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dachshund', 'scout')
describe_pet('scout', 'dachshund')
describe_pet('scout', 'dachshund')
############

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    #print(f"My {animal_type} 's name is {pet_name.title()} .")
    
describe_pet('dachshund', 'scout')
describe_pet('scout', 'dachshund')
 