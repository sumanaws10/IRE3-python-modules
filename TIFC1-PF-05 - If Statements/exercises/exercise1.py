#https://ehmatthes.github.io/pcc_3e/solutions/chapter_5/


#Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
#Task 1
dog = 'Johny'
print("Is dog == 'Sheru'? I predict False")
print(dog == 'Sheru')
print("Is dog == 'Johny'? I predict True")
print(dog == 'Johny')

#Task 2

age = 30
print("Is age != 10? I predict .")
print(age != 30)  # False

age = 30
print("Is age != 40? I predict True.")
print(age != 40)  # True

 #Task 3     
print ("Is age > 35? I predict False")
print(age > 35) #False

#Task 4
print ("Is age < 35? I predict True")
print(age < 35) #True

#task 5
print ("Is age <= 35? I predict True")
print(age <= 35) #True

#Task 6
print ("Is age >= 35? I predict False")
print(age >= 35) #False
#Task 7

print("Is age > 20 and age < 40? I predict True")
print(age > 20 and age < 40)
#Task 8
print("Is age < 5 or age > 100? I predict False")
print(age < 5 or age > 100)

#Task 9
 #Test 9: True - case-insensitive string comparison using lower()
food = "Pizza"
print("Is food.lower() == 'pizza'? I predict True.")
print(food.lower() == "pizza")  # True


Food = "Pizza"
print("Is food.lower() == 'pizza'? I predict True.")
print(Food.lower() == "pizza")  # True
# Test 10: False - checking a string starts with a particular substring
car = "subaru"
print("Does 'subaru' start with 't'? I predict False.")
print(car.startswith("t"))  # False

#If the person is less than 2 years old, print a message that the person is a baby.
# Set a value for the variable age
age = 30

# Use if-elif-else to determine the person's stage of life
if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

#Make a list of your three favorite fruits and call it favorite_fruits.
#Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is
#  in your list, the if block should print a statement, such as You really like bananas!
# Step 1: Make a list of your three favorite fruits
favorite_fruits = ["banana", "mango", "apple"]

# Step 2: Write five independent if statements to check for certain fruits
if "banana" in favorite_fruits:
    print("You really like bananas!")
elif "mango" in favorite_fruits:
    print("I love mango")
elif "apple" in favorite_fruits:
    print("I dont like apple")
elif "pinapple" not in favorite_fruits:
    print("sometime I love ")
else:
    print("Pinapple is not in your favorite list,! Sorry")



#################
# List of usernames including 'admin'
usernames = ["alice", "bob", "charlie", "admin", "dave"]

# Loop through the list and print a greeting for each user
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.capitalize()}, thank you for logging in again.")

    ##########################
    #Stretch and Challenge
    #####################
current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")



###############################
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
