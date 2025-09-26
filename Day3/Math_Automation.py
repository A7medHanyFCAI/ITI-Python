import math

def math_report():
    filename = "math_report.txt"
    
 
    while True:
        nums_input = input("Enter numbers separated by commas: ").strip()
        try:
            numbers = [float(x) for x in nums_input.split(",") if x.strip()]
            if not numbers:
                raise ValueError
            break
        except ValueError:
            print("Invalid input.")
    
    with open(filename, "w") as f:
        for num in numbers:
            f.write(f"Number: {num}\n")
            f.write(f"  Floor: {math.floor(num)}\n")
            f.write(f"  Ceil: {math.ceil(num)}\n")
            if num >= 0:
                f.write(f"  Square Root: {math.sqrt(num):.2f}\n")
            else:
                f.write("  Square Root: Not defined for negative numbers\n")
            f.write(f"  Area of Circle (r={num}): {math.pi * num * num:.2f}\n")
            f.write("-" * 40 + "\n")
    
  
    print(f"\n'{filename}' has been created with the results.\n")
    with open(filename, "r") as f:
        print(f.read())


if __name__ == "__main__":
    math_report()
