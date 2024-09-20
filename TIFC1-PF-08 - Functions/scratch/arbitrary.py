def dog_dinner(amount, *meats):
    """What goes into the dog's bowls?"""   # this is comments explaining what function does
    for meat in meats:  # amount is take positional argument 2
        print(f"I'm putting {amount} scoops of {meat} in each of your bowls")
        #print(meats)
#call the function
dog_dinner(2, 'chicken', 'kibble', 'gravy') # 2 is go to the amount and remaining items pass to meats