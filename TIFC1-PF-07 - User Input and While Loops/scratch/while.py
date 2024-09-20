prompt = "Hello Weasley and Noche! What would you like to eat today?"
prompt += "\nThis is what we have: tuna, chicken, salmon, and clams. Type 'done' when you are finished! \n"

while True:
    answer = input(prompt)
    if answer.lower() == 'tuna':
        print("That sounds great! I will make tuna for you now.")
    elif answer.lower() == 'chicken':
        print("I am surprised you chose chicken!")
    elif answer.lower() == 'salmon':
        print("Salmon is so special, yum!")
    elif answer.lower() == 'clams':
        print("Wow! Fancy clams!")
    elif answer.lower() == 'done':
        break
    else:
        print("Sorry! We do not have that.")
 