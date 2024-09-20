class Cat():
    #an attempt to model a cat
    def __init__(self, name, age):
        #assign the cats name and age
        self.name = name
        self.age = age

    def sleep(self):
        #The cat can sleep
        print(f"{self.name} is fast asleep like a little angel")

    def climb(self):
        #The cat can sleep
        print(f"Quick! {self.name} is climbing on the roof!")

my_cat = Cat('Weasley', 1)
print(my_cat.name)
print(my_cat.age)   # access the attribute from the class
#access the sleep method
my_cat.sleep()
# access the climb method
my_cat.climb()
print(f" My cat age is {my_cat.age} year old")
#my_cat = Cat('Weasely', 1)
#my_cat2 = Cat('Noche', 3)
#my_cat2.sleep()