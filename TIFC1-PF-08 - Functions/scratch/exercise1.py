1.#Write a function called display_message() that prints one sentence telling everyone what you are learning 
# about in this module. Call the function, and make sure the message displays correctly
def display_message(module):
    print("In this module, I am learning Python")
display_message('module')


2.#Write a function called favorite_book() that accepts one parameter, title. The function should print a
#  message, such as, “One of my favorite books is Alice in Wonderland.” Call the function, making sure to 
# include a book title as an argument in the function call.
def favorite_book(title):
    print("one of my favorite books is:", title)
favorite_book(' Alice in Wonderland.')

#  Write a function called make_shirt() that accepts a size and the text of a message
# Call the function once using positional arguments to make a shirt. Call the function a second time using
#  keyword arguments.
def make_shirt(size, message):
    print(f"A {size} shirt will be made with message: '{message}' ")

make_shirt("medium", "Hello")
make_shirt(size="small", message="Python is awesome!")


###################
def make_shirt(size="large", message="I love Python."):
    print(f"A {size} shirt will be made with the message: '{message}'.")

# Making a large shirt with default message
make_shirt()
make_shirt("medium")
make_shirt("small", "Keep calm and code on!")
###################
#Call your function for three different cities, at least one of which is not in the default country.
def describe_city(city, country= "Unknown"):
    print(f"A {city} s will be in: '{country}'.")

describe_city("Dublin")
describe_city("Paris", "France")
describe_city(city= "Dublin", country= "Ireland")
##########
