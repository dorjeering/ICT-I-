try:
    n = float(input("Enter a number: "))
    res = 100/n
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Entered an invalid number!")
except:
    print("An unexpected error occurred.")
else:
    print("The result is: ", res)
finally:
    print("Execution Complete.")