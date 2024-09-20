#filename = 'learning_python.txt'
with open ('IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/stratch/learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open ('IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/stratch/learning_python.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line)

with open ('IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/stratch/guest.txt') as file_object1:
    file_object1.write(input("Please Enter your name: "))

    

