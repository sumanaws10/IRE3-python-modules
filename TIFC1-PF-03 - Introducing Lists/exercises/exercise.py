#Store the names of a few of your favorite music artists in a list called names. Print each name by
#  accessing each element in the list, one at a time.

Names = ['Arijit Singh', 'Shreya Ghoshal', 'Sonu Nigum']
print(Names)
print(Names[0])
print(Names[-1])
print(Names[2])

#Start with the “names” list you used in the first exercise, but instead of just printing each name,
#  print a message to them. The text of each message should be the same, but each message should be 
# personalized with the music artist’s name.

Names = ['Arijit Singh', 'Shreya Ghoshal', 'Sonu Nigum']
print(f"Best singer {Names[0]}")
print(f"Best singer {Names[1]}")
print(f"Best singer {Names[2]}")
#Make a list that stores several examples. Use your list to print a statement about your favorite book or movie. For example, “My favorite book is Pride and Prejudice”.
#Add an author or director name! Try printing a message to the author or director on what you liked about their book or movie!

movie = ["3 Idiots", "Joker", "housefull", "Dhirshym"]

print(f"My favorite movie is: {movie[0]}")
print(f"My favorite movie is: {movie[1]}")
print(f"My favorite movie is: {movie[2]}")

# Dinner Problem
names = ['Swati', 'Aaksh', 'Geet', 'Ramya']
print(f"You are invited for dinner tonight: {names[0]}")
print(f"You are invited for dinner tonight: {names[1]}")
print(f"You are invited for dinner tonight: {names[2]}")
# Modifey list
names.insert(0, "Pinky")

print(names)
names.insert(2, "John")
names.append('Viaan')
print(names)
print(f"You are invited for dinner tonight: {names[0]}")
print(f"You are invited for dinner tonight: {names[1]}")
print(f"You are invited for dinner tonight: {names[2]}")
print(f"You are invited for dinner tonight: {names[3]}")
print(f"You are invited for dinner tonight: {names[4]}")
names.pop()
print(names)
names.pop(1)
names.pop(2)
print(names)
names.remove('Geet')
names.remove('John')
print(f"You are invited for dinner tonight: {names[0]}")
print(f"You are invited for dinner tonight: {names[1]}")
print(len(names))

