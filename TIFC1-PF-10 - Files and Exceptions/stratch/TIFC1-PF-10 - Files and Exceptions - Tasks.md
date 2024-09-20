# Files and Exceptions - Tasks

## 1. Learning Python
- Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far.
- Start each line with the phrase **In Python you can...**.
- Save the file as `learning_python.txt` in the same directory as your exercises from this chapter.
- Write a program that reads the file and prints what you wrote three times:
  - Print the contents once by reading the entire file.
  - Print the contents by looping over the file object.
  - Print the contents by storing the lines in a list and then working with them outside the `with` block.

## 2. Guest Name
- Write a program that prompts the user for their name.
- When they respond, write their name to a file called `guest.txt`.

## 3. Programming Reasons
- Write a while loop that asks people why they like programming.
- Each time someone enters a reason, add their reason to a file that stores all the responses.

## 4. File Reader with Error Handling
- Write a program that prompts the user to enter the name of a file.
- Try to open the file for reading.
- If the file does not exist, catch the `FileNotFoundError` exception and print a message indicating that the file could not be found.
- If the file exists, read its contents and display them.

## 5. Cats and Dogs
- Create two files: `cats.txt` and `dogs.txt`.
- Store at least three names of cats in the first file and three names of dogs in the second file.
- Write a program that tries to read these files and print the contents to the screen.
- Wrap your code in a `try-except` block to catch the `FileNotFoundError`, and print a friendly message if a file is missing.
- Move one of the files to a different location on your system, and ensure the code in the `except` block executes properly.
  - **Stretch and Challenge:** Modify your `except` block to fail silently if either file is missing.

## 6. Favorite Number
- Write a program that prompts the user for their favorite number.
- Use `json.dump()` to store this number in a file.
- Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”