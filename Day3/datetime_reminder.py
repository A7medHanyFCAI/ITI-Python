from datetime import datetime, date

def datetime_reminder():
    filename = "reminders.txt"
    
    while True:
        user_input = input("Enter a date (YYYY-MM-DD): ").strip()
        try:
            reminder_date = datetime.strptime(user_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    today = date.today()
    diff = (reminder_date - today).days
    
    if diff < 0:
        print("This date has already passed.")
    else:
      
        with open(filename, "a") as f:
            f.write(f"{reminder_date} -> {diff} days left\n")
        
        print(f"Reminder saved: {reminder_date} -> {diff} days left")
        
      
        print("\nCurrent reminders:\n")
        with open(filename, "r") as f:
            print(f.read())


if __name__ == "__main__":
    datetime_reminder()
