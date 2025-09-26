import csv
import random

def random_data_generator():
    filename = "random_numbers.csv"

    while True:
        try:
            n = int(input("How many random numbers to generate? ").strip())
            if n > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    numbers = [random.randint(1, 100) for _ in range(n)]

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["index", "value"])
        for i, num in enumerate(numbers, start=1):
            writer.writerow([i, num])

  
    avg = sum(numbers) / len(numbers)
    print(f"\n'{filename}' created.")
    print(f"Total numbers: {n}")
    print(f"Average value: {avg:.2f}")


if __name__ == "__main__":
    random_data_generator()
