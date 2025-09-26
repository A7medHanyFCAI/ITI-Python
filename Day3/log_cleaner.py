import re

def regex_log_cleaner():
    log_file = "access.log"
    output_file = "valid_emails.txt"

    logs = [
        "john.doe@example.com",
        "Failed attempt: not-an-email",
        "alice_smith@domain.org",
        "Random text without email",
        "help@service.net",
        "hello@@gmail.com",
        "mike@company.com",
        "Garbage text xyz@@",
        "jane.doe123@website.co.uk",
        "invalid@email@domain"
    ]

    with open(log_file, "w") as f:
        f.write("\n".join(logs))

    
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    valid_emails = set() 
    with open(log_file, "r") as f:
        for line in f:
            matches = re.findall(email_pattern, line)
            valid_emails.update(matches)

    
    with open(output_file, "w") as f:
        f.write("\n".join(sorted(valid_emails)))

    print(f"\n'{output_file}' created.")
    print(f"Found {len(valid_emails)} unique emails:\n")
    with open(output_file, "r") as f:
        print(f.read())


if __name__ == "__main__":
    regex_log_cleaner()
