my_list = []        #create empty list
print(my_list)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))


foods = ["tuna", "salmon", "mackerel", "trout"]

print(foods[1:2])   # slice out right and left.
print(foods[:2])    #slice  is use to  create a new list and a section of list
print(foods[0:1])   # if we want to copy a list use slice
print(foods[2:])    # slice use in loop through list
print(foods[:])
###############################
# if we dont want to use create a list use range . both slice and range are same

weasley_foods = ["tuna", "salmon", "mackerel", "trout"]
noche_foods = weasley_foods[:]

weasley_foods.append('chicken')
noche_foods.append('cheese')

print("The foods Weasley likes to eat is: ")
print(weasley_foods)

print("The foods Noche likes to eat is: ")
print(noche_foods)