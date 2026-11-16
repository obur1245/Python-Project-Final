
from shop import Shop


def add_new_customer(shop):
    print("ADD NEW CUSTOMER")

    last_name = input("Enter the customer's last name: ")
    phone_number = input("Enter the customer's phone number: ")

    shop.add_customer(last_name, phone_number)


def find_customer_menu(shop):

    print("FIND CUSTOMER")

    try:
        customer_id = int(input("Enter customer ID: "))
    except ValueError:
        print("Please enter a valid customer ID.")
        return

    customer = shop.find_customer(customer_id)

    if customer is not None:
        customer.display()
    else:
        print("Customer not found.")


def view_customer_rentals(shop):
    print("CUSTOMER RENTALS")

    try:
        customer_id = int(input("Enter customer ID: "))
    except ValueError:
        print("Please enter a valid customer ID.")
        return

    customer = shop.find_customer(customer_id)

    if customer is None:
        print("Customer not found.")
        return

    rentals = shop.find_rentals_for_customer(customer_id)

    if len(rentals) == 0:
        print("This customer has no rentals.")
    else:
        for rental in rentals:
            rental.display()


def view_open_rentals(shop):
    print("OPEN RENTALS")

    found_rental = False

    for rental in shop.rental_list:
        if not rental.isClosed:
            rental.display()
            found_rental = True

    if not found_rental:
        print("There are currently no open rentals.")


def create_new_rental(shop):
    print("CREATE NEW RENTAL")

    has_customer_id = input(
    ).lower().strip()

    if has_customer_id == "no":
        print("Please use the Add a New Customer option first.")
        return

    elif has_customer_id != "yes":
        print("Please enter yes or no.")
        return

    try:
        customer_id = int(input("Enter customer ID: "))

        skis = int(input("Number of skis to rent: "))

        snowboards = int(input("Number of snowboards to rent: "))

        hours = int(input("Number of rental hours: "))

    except ValueError:
        print("Please enter whole numbers for all rental amounts.")
        return

    shop.new_rental(customer_id, skis, snowboards, hours)


def return_rental(shop):
    print("RETURN RENTAL")

    try:
        rental_id = int(input("Enter rental ID: "))
    except ValueError:
        print("Please enter a valid rental ID.")
        return

    shop.complete_rental(rental_id)


def display_inventory(shop):
    shop.display_inventory()


def display_statistics(shop):
    shop.display_statistics()


def main():
    # Create the shop with its starting inventory.
    shop = Shop(20, 15)

    while True:
        print("SKI AND SNOWBOARD RENTAL")
        print("1. Add a New Customer")
        print("2. Find a Customer")
        print("3. View Customer Rentals")
        print("4. View All Open Rentals")
        print("5. Create a New Rental")
        print("6. Return a Rental")
        print("7. Display Inventory")
        print("8. View Shop Statistics")
        print("9. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            add_new_customer(shop)

        elif choice == "2":
            find_customer_menu(shop)

        elif choice == "3":
            view_customer_rentals(shop)

        elif choice == "4":
            view_open_rentals(shop)

        elif choice == "5":
            create_new_rental(shop)

        elif choice == "6":
            return_rental(shop)

        elif choice == "7":
            display_inventory(shop)

        elif choice == "8":
            display_statistics(shop)

        elif choice == "9":
            print("Thank you for using the rental shop!")
            break

        else:
            print("Invalid option. Please choose 1-9.")


# Start the application.
if __name__ == "__main__":
    main()
