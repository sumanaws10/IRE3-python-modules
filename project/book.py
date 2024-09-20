
def book_store():
    book_choice = input("Enter books title: ")
    book_price = input ("Enter books price: ")

    return "Title: " + book_choice + ", costs " + book_price


print (book_store())



############################
def menu():
  print("-- MENU--")
  print("1. Snacks")
  print("2. Mains")
  print("3. Drinks")
  print("4. View order")
  print("5. Exit")
  print()

def user_option():
  choice = int(input("Choose from the menu & enter a number 1-5: "))
  if choice == 1:
    print()
    print("MENU - here is Snacks")
    print("Salad - $5")
    print("Samosa - $6")
    print("Soup - $10")
  elif choice == 2:
    print("Main - here is Main Menu")
    print("Pasta - $13")
    print("Burger - $12")
    print("Pizza - $10")
  elif choice == 3:
    print("DRINKS - heres drinks")
    print("Water - $0")
    print("Tea - $3")
    print("Sprite - $2")
  elif choice == 4:
    print("VIEW ORDER -- heres ur order so far")
  elif choice == 5:
    print("Exiting")
  else:
    print("Invalid")
    choice = int(input("Enter number 1-5"))

def main():
  user_food = input("Choose which u want : ")
  if user_food == "pasta":
    cheese_2 = input("Cheese? yes/no ")
  elif user_food == "burger":
    onions = input("Onions? yes/no ")
  elif user_food == "Pizza":
    pizza = input("Cheese or pepperoni? ")
  else:
    print("Alright!")
  user_option()

print("Welcome to Shop!")
print()
user_option()
main()
