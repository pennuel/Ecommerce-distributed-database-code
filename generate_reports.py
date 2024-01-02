from db.customers_order_by_region import create_customer_report
from db.sales_report_by_region import create_sales_by_payment_per_region_report

def main():
    # Display menu to the user
    print("Choose a report to generate:")
    print("1. Customer Order Summary Report")
    print("2. Sales By Payment Per Region Report")

    # Get user input
    user_choice = input("Enter the number of the report you want to generate: ")

    # Execute the corresponding function based on user input
    if user_choice == "1":
        create_customer_report()
    elif user_choice == "2":
        create_sales_by_payment_per_region_report()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    # Run the main function if the script is executed
    main()