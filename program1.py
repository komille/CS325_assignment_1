print("Hello,")
number = input("Enter a number:\n")

while number.isnumeric()!= True:
    print("That's not a number")
    print("Try again")
    number = input("Enter a new number:\n")

print(f'Your number that you picked is {number}')
    
