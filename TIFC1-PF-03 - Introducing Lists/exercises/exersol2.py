#https://ehmatthes.github.io/pcc/solutions/chapter_3.html
#https://github.com/syedtahamashhadi/SSUET-Module_1a-Assignments/blob/master/Assignment_1.py

#Store the locations in a list. Make sure the list is not in alphabetical order.
#Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
#Use sorted() to print your list in alphabetical order without modifying the actual list.
location = ['France', 'Mount Abu', 'Germaney', 'london']
print(location)
print(sorted(location))
location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)

#Show that your list is still in its original order by printing it.
#Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#Show that your list is still in its original order by printing it again.
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.


names = ['mountains', 'rivers', 'countries', 'cities', 'languages']
print(names)
names[1]="English"
names[0]="Marwari"# changing first element of names from mountains to marwari
names[2]="Hindi"
names[3]="Gujrati"
print(names)
