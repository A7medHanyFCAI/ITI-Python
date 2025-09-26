import time
from Math_Automation import math_report
from log_cleaner import regex_log_cleaner

# ----------------------------
# Decorator definition
# ----------------------------
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        runtime = round(end - start, 4)
        log_entry = f"{func.__name__} executed in {runtime} seconds\n"

        with open("execution_log.txt", "a") as f:
            f.write(log_entry)

        print(f"[LOG] {log_entry.strip()}")
        return result
    return wrapper



@log_time
def decorated_math_report():
    math_report()

@log_time
def decorated_regex_cleaner():
    regex_log_cleaner()



def run_demo():
    """
    Runs two decorated tasks to verify logging.
    Logs will be written to execution_log.txt
    """
    print("\n=== Running Decorators Demo ===")
    decorated_math_report()
    decorated_regex_cleaner()
    print("Check 'execution_log.txt' for log entries.")
