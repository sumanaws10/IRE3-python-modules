class Cat():
    #an attempt to model a cat
    def __init__(self, name, age):
        #creates the instance and assign the cats name and age
        self.name = name
        self.age = age

    def sleep(self):
        #The cat can sleep. self just means this instance of the class. 
        print(f"{self.name} is fast asleep like a little angel")

    def climb(self):
        #The cat can sleep
        print(f"Quick! {self.name} is climbing on the roof!")

# creates an instance of the cat class and assigns it to
# the variable my_cat. self does not have an argument.
# self is used by the class, to determine what instance it is working on, and to allow the insnace to acecss
# the attributes and methods of the class.  
#main body of the program
my_cat = Cat('Weasley', 1)
print(my_cat.name)