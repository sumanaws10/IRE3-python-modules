##Stretch & Challenge
#https://github.com/LuckyLub/crashcourse/blob/master/20190227.py
#Write a function called make_great() that modifies the list of magicians by adding the phrase, 
# “the Great” to each magician’s name.
#Call show_magicians() to see that the list has actually been modified.
def  show_magicians(magician_names):
    for magician in magician_names:
        print('magician')


magician_names = ['Paul Daniels', 'David Blaine', 'Derren Brown', 'Harry Houdini']
show_magicians(magician_names)


###############
def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    # Build a new list to hold the great musicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Harry Houdini', 'David Blaine', 'Teller']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)


