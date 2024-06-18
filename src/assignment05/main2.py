# --------------------------------
# Title: Assignment 05
# Description: Mailroom

from thank-you_note import send_thank_you
from main import create_report

def main():

    MENU: str =\
    "--Welcome to the Mailroom--\n\
Select from the following menu\n\
1. Send a Thank You\n\
2. Create a Report\n\
3. Exit the Program"

    donor_list = [
        ("William Gates, III", [120.0, 100.0]),
        ("Jeff Bezos", [532.00, 1000]),
        ("Paul Allen", [633, 213.12]),
        ("Mark Zuckerberg", [733.12, 423.12, 932.23]),
    ]

    while True:
        print("\nMenu:")
        choice = input("Enter a menu choice (1/2/3): ").strip()

        if choice == "1":
            print("Sending a thank you...")
            send_thank_you()
        elif choice == "2":
            print("Creating a report")
            create_report()
        elif choice == "3":
            print("Quitting the program. Goodbye")

if __name__ == "__main__":
    main()