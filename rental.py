
class Rental:
    """Represents a ski and snowboard equipment rental."""

    # Class variable used to assign unique rental IDs.
    next_rental_id = 200

    def __init__(self, customer_id, skis_rented, snowboards_rented, rental_hours):

        self.rental_id = Rental.next_rental_id
        Rental.next_rental_id += 1

        self.customer_id = customer_id
        self.skis_rented = skis_rented
        self.snowboards_rented = snowboards_rented
        self.rental_hours = rental_hours

        # New rentals are open until the equipment is returned.
        self.isClosed = False

    def display(self)
        print(f"Rental ID: {self.rental_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Skis Rented: {self.skis_rented}")
        print(f"Snowboards Rented: {self.snowboards_rented}")
        print(f"Rental Length: {self.rental_hours} hours")

        if self.isClosed:
            print("Rental Status: CLOSED")
        else:
            print("Rental Status: OPEN")
