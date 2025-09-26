"""
Main entry point for Automation Project
---------------------------------------
- Imports all task modules.
- Displays a menu of available tasks.
- Runs the task selected by the user.
"""

# Import task modules
import Math_Automation
import log_cleaner
import datetime_reminder
import product_data_transformer
import os_file_manager
import random_data_generator
import execution_time   


def display_menu():
    """Display the available tasks to the user."""
    tasks = [
        "Math Automation",
        "Regex Log Cleaner",
        "Datetime Reminder Script",
        "Product Data Transformer",
        "OS File Manager",
        "Random Data Generator",
        "Decorators Demo (logs execution time)"
    ]
    print("\n=== Automation Tasks Menu ===")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("=============================")


def run_task(choice):
    """Run the selected task based on user input."""
    if choice == "1":
        Math_Automation.math_report()
    elif choice == "2":
        log_cleaner.regex_log_cleaner()
    elif choice == "3":
        datetime_reminder.datetime_reminder()
    elif choice == "4":
        product_data_transformer.product_data_transformer()
    elif choice == "5":
        os_file_manager.os_file_manager()
    elif choice == "6":
        random_data_generator.random_data_generator()
    elif choice == "7":
        execution_time.run_demo()
    else:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter the task number (or 'q' to quit): ").strip()
        if choice.lower() == "q":
            print("Exiting program.")
            break
        run_task(choice)
