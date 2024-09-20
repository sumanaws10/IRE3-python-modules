# Call the function three tiems, using a different number of arguments each time.
def make_sandwich(*items):
    print("I will make you a sanwich")
    for item in items:
        print("  ....adding " + item + "  your sandwich ")
    print("your sanwich is ready")
make_sandwich('cheese', 'potato', 'butter')
make_sandwich('Double cheese', 'Patties', 'vegetables')
make_sandwich('peanut butter', 'strawberry jam')

######################
