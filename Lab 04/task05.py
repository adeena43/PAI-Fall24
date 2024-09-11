#Write a Python class Restaurant with attributes like menu_items, book_table, and
#customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
#Perform the following tasks now:
# Now add items to the menu.
# Make table reservations.
# Take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.
#Note: Use dictionaries and lists to store the data
class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.table_reservations = []
        self.customer_orders = []

    def add_item_to_menu(self, name, price):
        self.menu_items[name] = price
        print(f"Added {name} to the menu with the price {price}")

    def book_table(self, table_number, customer_name):
        reservation = {'table number': table_number, 'customer name': customer_name}
        self.table_reservations.append(reservation)
        print(f"Table {table_number} reserved for {customer_name}")

    def customer_order(self, customer_name, items_ordered):
        order = {'customer name': customer_name, 'items': items_ordered}
        self.customer_orders.append(order)
        print(f"Order taken from {customer_name}")

    def print_menu(self):
        if not self.menu_items:
            print("Menu is empty.")

        else:
            print("Menu: ")
            for item, price in self.menu_items.items():
                print(f"{item}: ${price}")

    def print_table_reservations(self):
        if not self. table_reservations:
            print("No table reservations.")

        else:
            print("Table Reservations: ")
            for reservations in self.table_reservations:
                print(f"Table {reservations['table_number']} reserved for reservations['customer_name']")

    def print_customer_orders(self):
        if not self.customer_orders:
            print("No customer orders.")

        else:
            print("Customer orders: ")
            for order in self.customer_orders:
                for item in order['items']:
                    print(f"  -{item}")

restaurant = Restaurant()

restaurant.add_item_to_menu('Biryani', 220)
restaurant.add_item_to_menu('Burger', 350)
restaurant.add_item_to_menu('Shwarma', 160)

restaurant.book_table(1, "Jawad")
restaurant.book_table(2, "Sara")

restaurant.customer_order('Jawad', ["Biryani", "Shwarma"])
restaurant.customer_order('Sara', ["Burger", "Shwarma"])

restaurant.print_menu()

restaurant.print_table_reservations

restaurant.print_customer_orders
