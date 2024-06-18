# --------------------------------
# Title: Assignment 05
# Description: Mailroom
# --------------------------------

import main2

# Define the Data Variables
Donor_name: str = ''
csv_data: str = ''
donors: list = []
header: list = []


def send_thank_you():
    while True:
        donor_name = input("Enter the Donor name (type 'list' to see all donors): ").title()

        if donor_name == "list":
            print("----List of donors:----")
            for donor in donors:
                print(donor)
        elif donor_name in donors:
            print("This donor is on the donor list")
            break
        else:
            donors.append((donor_name, []))  # adding a new donor
            print("This is a first_time donor!")
            break

    amount = 0
    while True:
        amount_str = input("Enter donation amount: ").strip()
        if not amount_str.isdigit():
            print("Please enter a valid donation amount.")
            continue

        else:
            amount = int(amount_str)
            for i, donor in enumerate(donors):  # I being the index of components of donor_list
                if donor[0] == donor_name:
                    donors[i] = (donor_name, donor[1] + [amount])
                    print(f"{donor[0]}\'s donation of ${amount} has been recorded!")
                    break

    thank_you_email = f"""
    'Dear {donor_name},
    Thank you for your donation of ${amount}
    Thank you,
    Richard Khan - The Local Charity Team'"""

    print("_" * 50)
    print("The following email has been sent: ")
    print(thank_you_email)