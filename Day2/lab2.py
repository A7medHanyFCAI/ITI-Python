"""
    Python Practice Tasks
    =====================

    Rules:
        - Everything must be written inside functions.
        - The file should run as a script.
        - When the script starts, the user must see a menu of numbered scenarios  (1: List order, 2: People with favorite color , .....).
        - The user chooses a number, and the program runs the corresponding function.
        - Each task should only run when chosen from the menu.
        - At ANY stage: if the user enters invalid input, the program must:
              * Show an error message
              * Display what valid input looks like
              * Let the user try again (do not crash or exit)
"""
"""
    Tasks:
    ------

    1 - Ask the user to enter 5 numbers.
        Store them, then display them in ascending order and descending order.
"""
def task1():
    lst = []
    print("Please enter 5 numbers")
    for i in range(5):
        while True:
            try:
                num = float(input(f"Number {i+1}: "))
                break
            except ValueError:
                print("Invalid input!")

        lst.append(num)

    print(f"\nAscending order: {sorted(lst)}")
    print(f"Descending order: {sorted(lst, reverse=True)}")

"""
     2 - Write a function that takes two numbers: (length, start).
         Generate a sequence of numbers with the given length,
         starting from the given start number and increasing by one each time.
         Print the result.
"""
def task2():
    seq = []
    while True:
        try:
            length = int(input("Enter the sequence length: "))
            break
        except ValueError:
            print("Invalid input!")
    while True:
        try:
            start = int(input("Enter the starting number: "))
            break
        except ValueError:
            print("Invalid input!")
    for i in range(length):
        seq.append(start+i)

    print("\nGenerated sequence:", seq)
    
"""
     3 - Keep asking the user for numbers until they type "done".
        When finished, print:
             * The total of all numbers entered
             * The count of valid entries
             * The average
        If the user enters something invalid, show an error and continue.
"""
def task3():
    numbers = [] 
    print("Enter numbers one by one. Type 'done' when finished.")     
    while True:
        inp = input("Enter a number or 'done': ").strip().lower()
        if inp == "done":
            break
        try:
            numbers.append(float(inp))
        except ValueError:
            print("Invalid input!")

    if numbers:
        total = sum(numbers)
        count = len(numbers)
        avg = total / count
        print(f"Total: {total}, Count: {count}, Average: {avg:0.2f}")
    else:
        print("No numbers were entered.")

"""
     4 - Ask the user to enter a list of numbers.
         Remove any duplicates, sort the result, and display it.
"""
def task4():
    
    while True:
        try:
            print("Enter list numbers separated by spaces:")
            lst = sorted(set(map(float,input().split())))
            break
        except ValueError:
            print("Invalid input!")
    
    print(f"Sorted list without duplicates: {lst}")

"""   
     6 - Ask the user to enter a sentence.
         Count how many times each word appears in the sentence
         and display the result.
"""
def task6():
    words = input("Enter a sentence: ").lower().split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1 
    print()
    for word,count in word_count.items():
        print(f"{word}: {count}")
"""
     7 - Create a small grade book system:
         - The user enters 5 students names and their scores.
         - At the end, show:
            * The highest score
             * The lowest score
             * The average score.
"""
def task7():
    students = {}
    print("Enter 5 students names and their scores")
    for i in range(5):
        name = input(f"Enter student {i+1} name: ")
        while not name or not name.isalpha() :
            print("Please enter a valid name (only letters, not empty).")
            name = input(f"Enter student {i+1} name: ")
        while name in students:
            print("Name already exist")
            name = input(f"Enter student {i+1} name: ")
        while True:
            try:
                score = float(input(f"Enter student {i+1} score: "))
                break
            except ValueError:
                print("Please Enter a Valid Score")
        students[name] = score

    scores = list(students.values())
    print(f"\nHighest score: {max(scores)}")
    print(f"Lowest score: {min(scores)}")
    print(f"Average score: {sum(scores) / len(scores):0.2f}")
"""
     8 - Write a program that simulates a shopping cart:
         - The user can add items with a name and a price.
         - The user can remove items by name.
         - The user can view all items with their prices.
         - At the end, display the total cost.
"""
def task8():
    cart = {}
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. View items")
        print("4. Checkout and exit")

        choice = input("\nChoose an option: ").strip()
        if choice == "1":
            name = input("Enter item name: ")
            while not name or not name.isalpha() :
                print("Please enter a valid name (only letters, not empty).")
                name = input("Enter item name: ")
            while True:
                try:
                    price = float(input("Enter item price: "))
                    break
                except ValueError:
                    print("Invalid Price")
            cart[name] = price

        elif choice == "2":
            name = input("Enter item name to remove: ")
            if name in cart:
                del cart[name]
                print(f"Removed {name}.")
            else:
                print("Item not found in cart.")

        elif choice == "3":
            if cart:
                print()
                for item, price in cart.items():
                    print(f"{item}: {price}")
                print()
            else:
                print("Cart is empty.")

        elif choice == "4":
            total = sum(cart.values())
            print(f"\nTotal cost: ${total}\n")
            break
        else:
            print("Invalid Choice.\n")
"""
     9 - Create a number guessing game:
         - The program randomly selects a number between 1 and 20.
         - The user keeps guessing until they get it right.
         - After each guess, show if the guess was too high or too low.
         - When correct, display the number of attempts.
"""
import random

def task9():
    rand_num = random.randint(1,20)
    attempts = 0
    print("Guess the number (between 1 and 20).")
    while True:
        while True:
            try:
                guess = int(input("Your guess: "))
                break
            except ValueError:
                print("Invalid Guess")

        attempts += 1
        if guess < rand_num:
            print("Too low!")
        elif guess > rand_num:
            print("Too high!")
        else:
            print(f"\nCorrect! The number was {rand_num}. Attempts: {attempts}")
            break


while True:
    print("1. List Order")
    print("2. Sequence Generator")
    print("3. Average Calculator")
    print("4. Sorted Set")
    print("5. Words Counter")
    print("6. Grade System")
    print("7. Shopping Cart")
    print("8. Guessing Game")
    print("9. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print()
        task1()
        print()
    elif choice == "2":
        print()
        task2()
        print()
    elif choice == "3":
        print()
        task3()
        print()
    elif choice == "4":
        print()
        task4()
        print()
    elif choice == "5":
        print()
        task6()
        print()
    elif choice == "6":
        print()
        task7()
        print()
    elif choice == "7":
        print()
        task8()
        print()
    elif choice == "8":
        print()
        task9()
        print()
    elif choice == "9":
        break
    else:
        print()
        print("Invalid Choice.")
        print()

    