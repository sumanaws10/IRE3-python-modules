#Write a program that prompts the user to enter the name of a file. Try to open the file for reading.
#  If the file does not exist, catch the FileNotFoundError exception and print a message indicating that 
# the file could not be found. If the file exists, read its contents and display them. 

#filenames = ['cats.txt', 'dogs.txt']

filenames = ['IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/exercises/cats.txt',
             'IRE3-python-modules/TIFC1-PF-10 - Files and Exceptions/exercises/dogs.txt']

for filename in filenames:
    print("\nReading file: " + filename)
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")