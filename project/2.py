menu_prompt = """Please enter one of the following options:
- 'a' to add a book
- 'l' to list the books
- 's' to search for a book
- 'q' to quit
What would you like to do? """

selected_option = input(menu_prompt).strip().lower()

while selected_option != "q":
    if selected_option == "a":
        print("You selected 'a'.")
    elif selected_option == "l":
        print("You selected 'l'.")
    elif selected_option == "s":
        print("You selected 's'.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    # Allow the user to change their selection at the end of each iteration
    selected_option = input(menu_prompt).strip().lower()