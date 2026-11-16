
from customer import Customer
from rental import Rental


class Shop:

    def __init__(self, number_of_skis=20, number_of_snowboards=15):
        self.customer_list = []
        self.rental_list = []

        self.total_income = 0

        # Set up the starting equipment inventory.
        self.setup_inventory(number_of_skis, number_of_snowboards)

    def setup_inventory(self, intNumberOfSkis, intNumberOfSnowboards):
        if intNumberOfSkis < 0 or intNumberOfSnowboards < 0:
            print("Inventory cannot be negative.")
            return intNumberOfSkis

        self.number_of_skis = intNumberOfSkis
        self.number_of_snowboards = intNumberOfSnowboards

    def find_customer(self, intCustomerIDtoFind):
        for customer in self.customer_list:
            if customer.customer_id == intCustomerIDtoFind:
                return customer

        return None

    def find_rental(self, intRentalID):
        for rental in self.rental_list:
            if rental.rental_id == intRentalID:
                return rental

        return None

    def find_rentals_for_customer(self, intCustomerID):
        customer_rentals = []
        for rental in self.rental_list:
            if rental.customer_id == intCustomerID:
                customer_rentals.append(rental)

        return customer_rentals

    def add_customer(self, last_name, phone_number):
        new_customer = Customer(last_name, phone_number)

        self.customer_list.append(new_customer)

        print("Customer successfully added!")
        print(f"Your Customer ID is: {new_customer.customer_id}")

        return new_customer

    def new_rental(self, customer_id, skis_rented,
                   snowboards_rented, rental_hours):
        # Check that the customer exists.
        customer = self.find_customer(customer_id)

        if customer is None:
            print("Customer not found. Please check the customer ID.")
            return None

        # Check that rental amounts are valid.
        if (not isinstance(skis_rented, int)
                or not isinstance(snowboards_rented, int)
                or not isinstance(rental_hours, int)):
            print("Rental amounts and hours must be whole numbers.")
            return None

        if skis_rented < 0 or snowboards_rented < 0:
            print("Equipment amounts cannot be negative.")
            return None

        if rental_hours <= 0:
            print("Rental length must be at least one hour.")
            return None

        # Check that enough equipment is available.
        if skis_rented > self.number_of_skis:
            print("Not enough skis available.")
            return None

        if snowboards_rented > self.number_of_snowboards:
            print("Not enough snowboards available.")
            return None

        # Create the rental.
        new_rental = Rental(
            customer_id,
            skis_rented,
            snowboards_rented,
            rental_hours
        )

        self.rental_list.append(new_rental)

        # Remove rented equipment from inventory.
        self.number_of_skis -= skis_rented
        self.number_of_snowboards -= snowboards_rented

        print("Rental successfully created!")
        print(f"Your Rental ID is: {new_rental.rental_id}")

        return new_rental

    def complete_rental(self, intRentalID):
        rental = self.find_rental(intRentalID)

        if rental is None:
            print("Rental not found.")
            return None

        # Make sure the rental has not already been returned.
        if rental.isClosed:
            print("This rental has already been completed.")
            return None

        # Calculate the rental charge.
        ski_cost = rental.skis_rented * 15 * rental.rental_hours
        snowboard_cost = (
            rental.snowboards_rented * 10 * rental.rental_hours
        )

        total_charge = ski_cost + snowboard_cost

        # Return the equipment to inventory.
        self.number_of_skis += rental.skis_rented
        self.number_of_snowboards += rental.snowboards_rented

        # Add the payment to the shop's income.
        self.total_income += total_charge

        # Close the rental.
        rental.isClosed = True

        print("Rental successfully returned!")
        print(f"Total rental charge: ${total_charge:.2f}")

        return total_charge

    def display_inventory(self):
        print(f"Available Skis: {self.number_of_skis}")
        print(f"Available Snowboards: {self.number_of_snowboards}")

    def display_statistics(self):
        open_rentals = 0
        closed_rentals = 0

        for rental in self.rental_list:
            if rental.isClosed:
                closed_rentals += 1
            else:
                open_rentals += 1

        print(f"Total Income: ${self.total_income:.2f}")
        print(f"Total Customers: {len(self.customer_list)}")
        print(f"Total Rentals: {len(self.rental_list)}")
        print(f"Open Rentals: {open_rentals}")
        print(f"Completed Rentals: {closed_rentals}")

# Create the shop.
my_shop = Shop(20, 15)

# Add three customers.
customer1 = my_shop.add_customer("Smith", "555-111-2222")
customer2 = my_shop.add_customer("Johnson", "555-333-4444")
customer3 = my_shop.add_customer("Williams", "555-555-6666")

# Display customer information.
customer1.display()
customer2.display()
customer3.display()

# Create rentals.
rental1 = my_shop.new_rental(
    customer1.customer_id, 2, 1, 4
)

rental2 = my_shop.new_rental(
    customer2.customer_id, 3, 2, 3
)

rental3 = my_shop.new_rental(
    customer3.customer_id, 1, 1, 5
)

# Display rental information.
rental1.display()
rental2.display()
rental3.display()

# Display current inventory.
my_shop.display_inventory()

# Return the rentals.
my_shop.complete_rental(rental1.rental_id)
my_shop.complete_rental(rental2.rental_id)
my_shop.complete_rental(rental3.rental_id)

# Display final inventory and statistics.
my_shop.display_inventory()
my_shop.display_statistics()
