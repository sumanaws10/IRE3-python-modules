#Q.4 
filename = input("Please enter the name of the file you would like to open: ")

try:
    with open(filename, 'r') as file:
        contents = file.read()
        print("\n file contents:\n")
        print(contents)

except FileNotFoundError:
    print(f"Sorry, the file '{filename}' could not be found")