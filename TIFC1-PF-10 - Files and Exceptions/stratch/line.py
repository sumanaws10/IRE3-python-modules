with open('foods.txt') as file_object:
    for line in file_object:
        print(line)
 
with open('foods.txt') as file_object:
    lines = file_object.readlines()
 
for line in lines:
    print(line)
 
with open('foods.txt') as file_object:
    lines = file_object.readlines()
 
lines = [line.strip() for line in lines]
print(lines)
for line in lines:
    print(line)
 