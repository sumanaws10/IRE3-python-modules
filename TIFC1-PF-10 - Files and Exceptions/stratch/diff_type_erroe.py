try:

    # Code that may raise an exception

    result = 10 / 0  # This will raise a ZeroDivisionError

except ZeroDivisionError:

    print("You cannot divide by zero.")

except ValueError:

    print("Value error occurred.")

except Exception as e:  # Catch any other exception

    print(f"An error occurred: {e}")

 