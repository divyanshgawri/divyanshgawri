from fg import *
import time

# Define a list to store donation data
donation_data = []



# Function to process donations
def process_donation():
    name = input("Enter your name: ")
    amount = float(input("Enter the annual income : "))

    # Check if the user has made a previous donation
    for donation in donation_data:
        if donation["name"] == name:
            donation["amount"] = amount
            print(f"Your annual income  has been updated to ${amount}.")
            break
    else:
        donation_data.append({"name": name, "amount": amount})
        print("Thank you for your telling your salary!")


# Function to view donation data
def view_donations():
    if len(donation_data) == 0:
        print("PLS ENTER YOUR DATA FIRST")
    for donation in donation_data:
        print(f"Name: {donation['name']}, Amount: RS. {donation['amount']}")
#data showing
#data showing
def tell_data():
    tell = input("Tell your choice that you want data in hindi or english :"
                 "\n Press 1 for English"
                 "\n Press 2 for Hindi ")
    tell = int(tell)  # Convert the input to an integer
    if tell == 1:
        with open("dishu.txt",'r') as dg:
            fer = dg.readlines()
            for line in fer:
                print(line)
    elif tell == 2:
        with open("hindi.txt",'r',encoding='utf-8') as hg:
            fer2 = hg.readlines()
            for lines in fer2:
                print(lines)
    else:
        print("Invalid choice. Please enter 1 or 2.")



# Main program loop
while True:
    print("\nDonation Management System")
    print("1. Enter a salary")
    print("2. View salary")
    print("3. Exit")
    print("4. To Get Data In Text Form")
    print("5 To calculate the tax ")

    choice = input("Enter your choice: ")

    if choice == "1":
        process_donation()
    elif choice == "2":
        time.sleep(0.45)
        view_donations()
    elif choice == "3":
        break
    elif choice=="4":
        tell_data()
    elif choice == "5":
        from fg import calculate_tax


        def main():
            salary = float(input("Enter your salary: "))
            donation = float(input("Enter the amount you donated or any other deductions: "))
            final_tax = calculate_tax(salary, donation)
            print(f"Your total taxable income after deductions: {salary - donation}")
            print(f"Your tax to be paid: {final_tax}")


        if __name__ == "__main__":
            main()


    else:
        print("Invalid choice. Please try again.")

