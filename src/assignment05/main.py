# Title: Assignment 05
# Desc: Mailroom


# Define the Data Variables
Donor_name: str = ''
csv_data: str = ''
donors: list = []
header: list = []


def create_report():
    report_data = []

    # Print report header
    print("\n Donor Name | Total Donated  | Num Donations | Avg Donations ")
    print("------------------------------------------------------------")
    for donor, donations in donors:
        total_donated = sum(donor["donations"])
        num_donations = len(donor["donations"])
        avg_donation = total_donated / num_donations
        report_data.append((donor[0], total_donated[1], num_donations[2], avg_donation[3]))
    print(f"{[Donor_name]:<15}  | ${total_donated:<15.2f} | {num_donations:<15}  | ${avg_donation:<.2f}")




