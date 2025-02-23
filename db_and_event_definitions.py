# List of registered customerIDs
CUSTOMERS_DATABASE = [
    "customer-1",
    "customer-2",
    "customer-3",
    "customer-4",
    "customer-5",
    "customer-6"
]

# List of ride IDs with cost of each
RIDES_DATABASE = {
    "ride-a": 5,
    "ride-b": 10,
    "ride-c": 15,
    "ride-d": 15,
    "ride-e": 20
}


class TicketEvent:

    def __init__(self, customer_id, ride_number, purchase_time):
        self.customer_id = customer_id
        self.ride_number = ride_number
        self.purchase_time = purchase_time


class CustomerEvent:

    def __init__(self, customer_id, ride_number, cost, purchase_time):
        self.customer_id = customer_id
        self.ride_number = ride_number
        self.cost = cost
        self.purchase_time = purchase_time
