#favorite_foods = ['tuna', 'salmon', 'sardines', 'mackerel']

#for food in favorite_foods:         #food is temparary variable
   # print(food)
foods = ["tuna", "salmon", "mackerel", "trout"]

print("Okay Weasley, you can eat any of the following for dinner:")

for food in foods:
    print("You can have " + food + " for dinner. ")
    print("or....")
   
print("Nothing!")
######
cats = ["Poppy", "Molly", "Daisy", "Bella"]

print("Okay Viaan, you can take any of the following for playing:")

for cat in cats:
    print("You can take " + cat + " for playing. ")
    print("or....")
   
print("Nothing!")

######
Flights = ["Ryan", "Emirates", "Aerlingus", "BritishAirways"]
 
print("Next departing flights")
 
for flight in Flights:
    print(f"Next flight is  {flight} for takeoff ")
    print("then")
   
print("All flights departed!")