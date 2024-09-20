
#https://gist.github.com/jmangrad/849da723914003681f7c58b870bfbe8a
#Create a list of three kinds of your favorite pizza.
favorite_pizzas = ['Garlic Bread', 'Vegetarian Pizza', 'Topping Pizza']
#print("Pizza is my all time favorite food")
for pizza in  favorite_pizzas:
        print(pizza)
       # print("\n")

#For each pizza one line of output containing a simple statement like I like  pizza.
for pizza in favorite_pizzas:
        print(' I really love pizza ' + pizza + ' with cold drink ')
       
##########################################

pizzas = ["less cheese", "pineapple", "no pepperroni"]

for pizza in pizzas:
    print(pizza)
    print("A pizza should have {} ".format(pizza))
    
print("I really like pizza")
#Modify your program to print a statement about each animal, such as A dog would make a great pet.
animals = ["dog", "lion", "tiger"]
for animal in animals:
    #print(animal.title())
    
    print("{} has four legs".format(animal.title()))
print("All these have tails")

######
#Use a for loop to print the numbers from 1 to 20, inclusive.
numbers = list(range(1,20))
print(numbers)

#Make a list of the numbers from one to one million, and then use min() and max() to make sure your 
# list actually starts at one and ends at one million. Also, use the sum() function to see how quickly 
# Python can add a million numbers.

numbers = list(range(1, 1000000))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list

multiply = list(range(3,30,3))

for number in multiply:
    print(number)