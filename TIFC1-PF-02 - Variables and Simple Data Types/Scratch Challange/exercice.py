#Store a message in a variable, then print that message.
#Store a message in a variable, and print that message. Then change the value of your variable to a new
#  message, and print the new message.

message = ("This is my first exercise")
print(message)
msg = 'I love Python'
print(msg)
Name = 'Viaan'
age = '2'
print(Name, age)

msg1 = str(Name) + str(age) 
print(msg1)
#Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
personname = 'Tom'

print(personname.lower())
print(personname.upper())
print(personname.title())
#Write addition, subtraction, multiplication, and division operations that each result in the number 8. 
# Be sure to enclose your operations in print statements to see the results.
addition = 5 + 3
subtraction = 14 - 6
multiplication = 4 * 2
division = 16 / 2

print(addition)
print(subtraction)
print(multiplication)
print(division)
#Store your favorite number in a variable. Then, using that variable, create a message that reveals 
# your favorite number. Print that message.
favorite_num = 10
msg = "This is my number"+ str(favorite_num)
print(msg)

#Use an f-string to print out a message with a variable.

x = "Good"
y = "Day"
name = "Suman"
print(f"{x} {y} {name}")