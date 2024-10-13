#Question 3 Task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def add_orders(orders, customer, order_details, quantity):
    new_order = (customer, order_details, quantity)
    print("New Order Added!!")
    orders.append(new_order)

def display_orders(orders, customer, order_details, quantity):
    print("All orders: ")
    for order in orders:
        (customer, order_details, quantity) = order
        print(f"Customer: {customer}, Order Item: {order_details}, Quantity: {quantity}")
    
def main():

    while True:
        print("\nOrder System \n1. Add Order\n2. Display Orders\n3. Exit")
        choice = input("Please choose number (1-3)")
        
        if choice == '1':
            customer = input("Please enter customer name: ")
            order_details = input("Please enter order selection: ")
            quantity = input("Please enter order quantity: ")
            add_orders(orders, customer, order_details, quantity)
        elif choice == '2':
            display_orders(orders, customer, order_details, quantity)
        elif choice == '3':
            print("Thank you for placing your order!!")
            break
        else:
            print("Not a valid entry. Please try again.")
            
main()