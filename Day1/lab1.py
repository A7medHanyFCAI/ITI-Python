
import math
# - write a program that prints hello world
print("Hello World")
# 	- application to take a number in binary form from the user, and print it as a decimal
while True:
    try:
        binary_num = input("Enter a binary number: ")
        decimal_num = int(binary_num,2)
        break
    except ValueError:
        print("The binary number should only contians 1s and 0s")
        
print(f"Binary: {binary_num} => Decimal: {decimal_num}")

# 	- write a function that takes a number as an argument and if the number
# 		divisible by 3 return "Fizz" and if it is divisible by 5 return "buzz" and if is is
# 		divisible by both return "FizzBuzz"
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return 'The number you entered is not divisible by 3 or 5'
    
while True:
    try:
        number = float(input("Enter a Number: "))
        break
    except ValueError: 
        print("Please Enter a Valid Number")
print(fizzbuzz(number))

# 	- Ask the user to enter the radius of a circle print its calculated area and circumference


while True:
    try:
        radius = float(input("Enter the radius of the circle: "))
        break
    except ValueError:
        print("Invalid radius entered.")
        
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
# 	- Ask the user for his name then confirm that he has entered his name (not an empty string/integers). then proceed to ask him for his email and print all this data

name = input("Enter your name: ").strip()
while not name or not name.isalpha():
    print("Please enter a valid name (only letters, not empty).")
    name = input("Enter your name: ").strip()


email = input("Enter your Email: ").strip()
while not email or "@" not in email:
    print("Please enter a valid email. Your Email should contain '@'")
    email = input("Enter your Email: ").strip()

print(f"Name: {name}")
print(f"Email: {email}")

# 	- Write a program that prints the number of times the substring 'iti' occurs in a string

text = input("Enter a string: ")
count_iti = text.count("iti")
print(f"The substring 'iti' occurs {count_iti} times in the given string.")



