fridge = ['chicken', 'beef', 'sausages'] # define two lists
empty_items = []

def eat_food(name, foods):      #function is eat_food and two parameter is anme , food
    print(foods)
    for food in foods:      # food is temparary variable
        print(f"{name} is eating {food}")  
        empty_items.append(food)
        fridge.remove(food)     # remove the food from the fridge list

cooked = fridge[:]
eat_food('Scout', cooked)   # scout is argument and cooked is new list
for item in empty_items:
    print(f"You've eaten all of the {item}!")
if not fridge:
    print("\nYou've eaten everything in the house!")