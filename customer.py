
class Customer:
    # Class variable used to assign unique customer IDs.
    next_customer_id = 100

    def __init__(self, last_name, phone_number):
        self.last_name = last_name
        self.phone_number = phone_number

        # Assign a unique customer ID.
        self.customer_id = Customer.next_customer_id
        Customer.next_customer_id += 1

    def display(self):
        print("------------------------------")
        print("       CUSTOMER INFORMATION")
        print("------------------------------")
        print(f"Customer ID: {self.customer_id}")
        print(f"Last Name: {self.last_name}")
        print(f"Phone Number: {self.phone_number}")
        print("------------------------------")
