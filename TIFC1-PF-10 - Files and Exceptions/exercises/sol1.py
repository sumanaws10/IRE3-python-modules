with open('IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/exercises/learning_python.txt', 'w') as file:
    file.write("In Python you can write clean and readable code.\n")
    file.write("In Python you can work with different data structure.\n")
    file.write("In Python you can handle exceptions eaisly. \n")
    file.write("In Python you can use libraries to extend functionality. \n \n")

#filename = 'learning_python.txt'
filename = 'IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/exercises/learning_python.txt'
#.1 Reading the entire file content
with open(filename) as file:
    contents = file.read()
print(" Reading the entire file content:\n")
print(contents)

# 2. Looping over the file object line by line
print("Reading line by line using loop: \n")
with open(filename) as file:
    for line in file:
        print(line.strip()) # using strip() to remove extra newlines

#########################
#Q. 2 Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.  
name = input("Please enter your name: ")
with open('IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/exercises/guest.txt', 'w') as file:
    file.write(name)
print(f"Hello {name}! your name has been written to guest.txt")