menu_prompt = """Please enter one of the following options:
- 'To add a book:'
-'List the books:'
- 'Search for a book:'
- 'quit'
What would you like to do? """

# Get a selection from the user
selected_option = input(menu_prompt).strip().lower()

# Run the loop until the user selected 'q'
while selected_option != "quit":
    if selected_option == "To add a book":
        print("You selected 'to add a book'.")
    elif selected_option == " List the books: ":
        print("You selected ' List the books:'.")
    elif selected_option == "Search for a book:":
        print("You selected 'Search for a book:'.")
    else:
        print(f"Sorry, '{selected_option}' isn't a valid option.")

    # Allow the user to change their selection at the end of each iteration
    selected_option = input(menu_prompt).strip().lower()