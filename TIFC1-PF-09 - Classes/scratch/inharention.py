class Cat():
   #An attempt to model a cat
   def __init__(self, name, age):
       #assign the cats name and age
       self.name = name
       self.age = age
       self.animal_type = 'cat'

   def sleep(self):
       #The cat can sleep
       print(f"{self.name} is fast asleep like a little angel")

   def climb(self):
       #The cat can sleep
       print(f"Quick! {self.name} is climbing on the roof!")

   def animal_species(self, species):
       self.animal_type = species
       print(f"{self.name} is a {self.animal_type}")

class Tiger(Cat):
   #A different type of cat
   def __init__(self, name, age):
       super().__init__(name, age)
       self.foods = 'gazelle'
       self.animal_type = 'tiger'
    
   def food_pref(self):
       print(f"{self.name} does not want cat food he likes {self.foods}")
   
bob_tiger = Tiger('Bob', 12)
bob_tiger.sleep()
bob_tiger.food_pref()