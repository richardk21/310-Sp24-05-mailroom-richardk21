# Title: Assignment 05
# Desc: Mailroom

file_reference = open("Donors.csv", 'r')

# Define the Data Variables
Donor_name: str = ''
csv_data: str = ''
donors: list = []

# Option 1: Send Thank You note

# Function to find a donor by name
def find_donor(Donor_name):
    for donor in donors:
        if donor["Donor_name"].lower() == Donor_name.lower():
            return donor
    return None

# Function to print list of donors
def print_donor_list():
    print("\nList of Donors: ")
    for donor in donors:
        print(donor["Donor_name"])
    print()

# Function to send a thank you
def send_thank_you():
    while True:
        Donor_name = input("Enter the Donor name: ").strip()

        if Donor_name.lower() == "list":
            print_donor_list()
        else:
            donor = find_donor(Donor_name)
            if donor:
                donation = input("Enter the donation amount: ")
                donor["donation"].append(donation)
                print(f"Thank you {Donor_name} for your generous donation of ${donation}, but more is needed")

# Option 2: Create a report

def create_report():
    print("\nDonor Name | Total Given  | Num Donations | Avg Donations ")
    print("------------------------------------------------------------")
    for donor, donations in donors:
        total_donated = sum(donor["donations"])
        num_donations = len(donor["donations"])
        avg_donation = total_donated / num_donations
    print(f"{donor[Donor_name]:<15}  | ${total_donated:<15.2f} | {num_donations:<15}  | ${avg_donation:<.2f}")

# Main program
while True :
    print("\nMenu:")
    print("1. Send a thank you")
    print("2. Create a report")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        print("Sending a thank you...")
        send_thank_you()
    elif choice == "2":
        print("Creating a report")
        create_report()
    elif choice == "3":
        print("Quitting the program. Goodbye")



