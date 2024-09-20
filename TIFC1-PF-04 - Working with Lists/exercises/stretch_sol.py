#https://ehmatthes.github.io/pcc_3e/solutions/chapter_4/

#Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#Add a new pizza to the original list.
#Add a different pizza to the list friend_pizzas.
#Prove that you have two separate lists. Print the message, My favorite pizzas are:, 
# and then use a for loop to print the first list. Print the message, My friend’s favorite pizzas are:,
#  and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.
my_pizzas = ['Garlic Pizza', 'Veggie Pizza', 'Less cheese Pizza']
friend_pizzas = my_pizzas[:]

print(friend_pizzas)
my_pizzas.append('Pineapple pizza')
friend_pizzas.append('Toping Pizza')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
print("My friend favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

#A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
#Use a for loop to print each food the restaurant offers.
#Try to modify one of the items, and make sure that Python rejects the change.
food_tuple = ['Halwa', 'Paneer', 'Manchurian', 'Samosa', 'Panipuri']
print(food_tuple)

print("You can choose from the following menu items:")
for item in food_tuple:
    print(item)
    #print(f"- {item}")
food_tuple = ['Halwa', 'Paneer', 'Manchurian', 'Samosa', 'Chicken', 'Fish']
print("Our menu has been updated.")
print("You can now choose from the following items:")
for item in food_tuple:
    print(f"- {item}")