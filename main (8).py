number=int(input("Enter a number:"))
def check_odd_or_even():
    global number
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
check_odd_or_even()


        