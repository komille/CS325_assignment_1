print("Hello,")
number = input("Enter a number:\n")

while number.isnumeric()!= True:
    print("That's not a number")
    print("Try a number this time")
    number = input("New number:\n")

print(f'Your number that you picked is {number}')
    
