#Write a while loop that asks people why they like programming. Each time someone enters a reason,
#  add their reason to a file that stores all the responses. 

with open('programming_reasons.txt', 'a') as file:
    while True:
        reason = input("why do you like programming?")

        if reason.lower() == 'q':
            print("Thank you for your response !")
            break

        file.write(reason + '\n')
        print("Your reason has been added to the file.\n")


 