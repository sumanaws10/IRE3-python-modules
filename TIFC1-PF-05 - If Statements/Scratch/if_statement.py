foods = ['tuna', 'mackerel', 'salmon', 'sardines']

answer = input("What would you like to eat today boys?\n")

if answer.lower() == 'tuna':
    print(f"Okay, let's have {foods[0]} for dinner!" )
elif answer.lower() == 'mackerel':
    print(f"Okay, let's have {foods[1]} for dinner!")
elif answer.lower() == 'salmon':
    print(f"Okay, let's have {foods[2]} for dinner!")
elif answer == foods[3]:
    print(f"Okay, let's have {foods[3]} for dinner!")
else:
    print("Sorry boys! I only have chicken for dinner!")

########################
food = input("What would you like to order? \n")

if food.lower() == 'croissant':
    print("You have bought a croissant!")
###################################
food = input("What would you like to order? \n")

if food.lower() == 'croissant':
    print("You have bought a croissant!")
if food.lower() != 'croissant':
    print("Apologies, but we only sell croissants") 
#####################
#Checking Whether an Item is not in a list
foods = ['tuna', 'sardines', 'chicken', 'beef']
#unhappy_foods = 'avocado'
unhappy_foods = input("Please enter your unhappy food !")

if unhappy_foods not in foods:
    print(unhappy_foods + " is not on the list, sorry!")

foods = ['tuna', 'sardines', 'chicken', 'beef', 'avocado']
#unhappy_foods = 'avocado'
unhappy_foods = input("Please enter your unhappy food !")

if unhappy_foods not in foods:
    print(unhappy_foods + " is not on the list, sorry!")
else:
    print("Hooray we have it!")

######Having Multiple Lists!
available_foods = ['tuna', 'sardines', 'halloumi', 'chicken', 'beef', 'salmon', 'avocado']
disliked_foods = ['chicken', 'beef', 'turkey', 'bacon']

for food in available_foods:
    if food in disliked_foods:
        print(f"I know you don't like this, but it is good for you!!")
    else:
        print(f"Yay! We have something you like!")
       
print("No more food! Goodbye!")