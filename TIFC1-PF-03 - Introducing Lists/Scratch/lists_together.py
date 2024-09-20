#https://github.com/syedtahamashhadi/SSUET-Module_1a-Assignments/blame/master/Assignment_1.py

# Every Function: Think of something you could store in a list . For example, you could make a list of mountains, rivers, countries,
#  cities, languages, or anything else you’d like .
#Write a program that creates a list containing these items and then uses each function introduced in 
# this chapter at least once .

x=["cat",2.5,500,True]
print(x)
x[1]="dog" # changing first element of x from 2.5 to dog
print(x)

x=["cat","Lion", "Tiger"]
x.insert(0,"dog")#its insert the element in given position
print(x)

x.append('pig')#it will append the element at last
print(x)

bike=["honda","yamaha","suzuki"]
del bike[1] #deleting the value at index 1 from x
print(bike)

x.pop(2)  #it will pop that element out at given index and remove from that list If no index is specified ,
            #list.pop() removes the last item in the list#you can also play with that pop out no
print(x)
x.remove('pig')#it will remove the given elment from the list
print(x)

list_one = [1, 2, 3, 4, 5, 6, 7]  # This is the first list
list_two = [10, 12, 14]           # This is the second list
list_one.extend(list_two)         # Extend list_one by appending all items of list_two
print(list_one)

my_list = [2, 3, 5, 7, 11, 13] # Create a list
my_list.clear()                # Remove all the items from the list
print(my_list) 

my_list = ["Python", "is", "awesome", "Java", "is", "Alright"]# Create a list
my_index = my_list.index("is")                                # Return the index of the first "is"
print("The item was first found at index:", my_index)

##############################
my_list = ["mew", "mew", "kitten", "mew", "mew"]                  # Create a list
my_count = my_list.count("mew")                                   # Return the number of times "mew" appears
print("The number of times the item appeared was:", my_count)

my_list = ["zero", "one", "two", "three", "four", "five"]        # Create a list
my_list.reverse()                                                # Reverse the items of the list in place
print("Reversed list looks like:", my_list)

my_list.sort(reverse=True)                             #it will sort list in descending order
print(my_list)

my_list.sort()                             #it will sort list in ascending order
print(my_list)

original_list = ["zero", "one", "two", "three"]        # Create a list
copied_list = original_list.copy()                     # Copy the original list and return it.        
print("Copied list looks like:", copied_list)


my_list = [5, 3, 6, 1, 2, 4, 7]                  # Create a list
sorted(my_list, reverse=True)             # Sorted the items of the list in sort the item permenantlyorder
print("Sorted list looks like:", my_list)

my_list=['a','g','d','f','t','x','l']
my_list.sort()
print(my_list)