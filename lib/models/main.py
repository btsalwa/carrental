import click
from models import Customer, CarStore, Rental

@click.group()
def cli():
    pass

def display_main_menu():
    print("\nMain Menu:")
    print("1. Customers")
    print("2. Car Stores")
    print("3. Exit")

@cli.command()
def run():
    while True:
        display_main_menu()
        try:
            choice = click.prompt("Enter your choice", type=int)
            if choice == 1:
                customer_menu()
            elif choice == 2:
                car_store_menu()
            elif choice == 3:
                print("Exiting...")
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(str(e))

def display_customer_menu():
    print("\nCustomer Menu:")
    print("1. Add Customer")
    print("2. Delete Customer")
    print("3. Show All Customers")
    print("4. View Customer's Cars")
    print("5. Back to Main Menu")

def customer_menu():
    while True:
        display_customer_menu()
        try:
            choice = click.prompt("Enter your choice", type=int)
            if choice == 1:
                add_customer()
            elif choice == 2:
                delete_customer()
            elif choice == 3:
                show_customers()
            elif choice == 4:
                view_customer_cars()
            elif choice == 5:
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(str(e))

def add_customer():
    try:
        name = click.prompt("Enter customer name")
        rent_type = click.prompt("Enter rent type (1: hourly, 2: daily, 3: weekly)", type=int, default=1, show_default=True)
        rent_period = click.prompt("Enter rent period in hours/days/weeks", type=int, default=1, show_default=True)
        customer = Customer(name, rent_type, rent_period)
        customer.save()
        print("Customer added successfully.")
    except ValueError as e:
        print(str(e))

def delete_customer():
    try:
        customer_id = click.prompt("Enter customer ID to delete", type=int)
        customer = Customer.find_by_id(customer_id)
        if customer:
            customer.delete()
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")
    except ValueError as e:
        print(str(e))

def show_customers():
    customers = Customer.get_all()
    if not customers:
        print("No customers found.")
    else:
        for customer in customers:
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Rent Type: {customer.rent_type}, Rent Period: {customer.rent_period}")

def view_customer_cars():
    try:
        customer_id = click.prompt("Enter customer ID to view cars", type=int)
        customer = Customer.find_by_id(customer_id)
        if customer:
            customer.show_cars()
        else:
            print("Customer not found.")
    except ValueError as e:
        print(str(e))

def display_car_store_menu():
    print("\nCar Store Menu:")
    print("1. Add Car Store")
    print("2. Delete Car Store")
    print("3. Show All Car Stores")
    print("4. View Car Store's Cars")
    print("5. Back to Main Menu")

def car_store_menu():
    while True:
        display_car_store_menu()
        try:
            choice = click.prompt("Enter your choice", type=int)
            if choice == 1:
                add_car_store()
            elif choice == 2:
                delete_car_store()
            elif choice == 3:
                show_car_stores()
            elif choice == 4:
                view_car_store_cars()
            elif choice == 5:
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(str(e))

def add_car_store():
    try:
        store_id = click.prompt("Enter store ID")
        car_type = click.prompt("Enter car type")
        number_of_cars = click.prompt("Enter number of cars", type=int, default=0, show_default=True)
        hourly_rental_rate = click.prompt("Enter hourly rental rate", type=float, default=0.0, show_default=True)
        car_store = CarStore(store_id, car_type, number_of_cars, hourly_rental_rate)
        car_store.save()
        print("Car Store added successfully.")
    except ValueError as e:
        print(str(e))

def delete_car_store():
    try:
        store_id = click.prompt("Enter store ID to delete", type=int)
        car_store = CarStore.find_by_id(store_id)
        if car_store:
            car_store.delete()
            print("Car Store deleted successfully.")
        else:
            print("Car Store not found.")
    except ValueError as e:
        print(str(e))

def show_car_stores():
    car_stores = CarStore.get_all()
    if not car_stores:
        print("No car stores found.")
    else:
        for car_store in car_stores:
            print(f"ID: {car_store.store_id}, Car Type: {car_store.car_type}, Number of Cars: {car_store.number_of_cars}, Hourly Rental Rate: {car_store.hourly_rental_rate}")

def view_car_store_cars():
    try:
        store_id = click.prompt("Enter store ID to view cars", type=int)
        car_store = CarStore.find_by_id(store_id)
        if car_store:
            car_store.show_cars()
        else:
            print("Car Store not found.")
    except ValueError as e:
        print(str(e))

def display_rental_menu():
    print("\nRental Menu:")
    print("1. Add Rental")
    print("2. Show All Rentals")
    print("3. Calculate Total Rental Amount")
    print("4. Back to Main Menu")

def rental_menu():
    while True:
        display_rental_menu()
        try:
            choice = click.prompt("Enter your choice", type=int)
            if choice == 1:
                add_rental()
            elif choice == 2:
                show_rentals()
            elif choice == 3:
                calculate_total_rental_amount()
            elif choice == 4:
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(str(e))

def add_rental():
    try:
        rental_id = click.prompt("Enter rental ID")
        customer_id = click.prompt("Enter customer ID", type=int)
        store_id = click.prompt("Enter store ID", type=int)
        car_id = click.prompt("Enter car ID", type=int)
        start_date = click.prompt("Enter start date (format: YYYY-MM-DD)", type=str)
        end_date = click.prompt("Enter end date (format: YYYY-MM-DD)", type=str)
        rental = Rental(rental_id, customer_id, store_id, car_id, start_date, end_date)
        rental.save()
        print("Rental added successfully.")
    except ValueError as e:
        print(str(e))

def show_rentals():
    rentals = Rental.get_all()
    if not rentals:
        print("No rentals found.")
    else:
        for rental in rentals:
            print(f"ID: {rental.rental_id}, Customer ID: {rental.customer_id}, Store ID: {rental.store_id}, Car ID: {rental.car_id}, Start Date: {rental.start_date}, End Date: {rental.end_date}")

def calculate_total_rental_amount():
    try:
        customer_id = click.prompt("Enter customer ID to calculate total rental amount", type=int)
        customer = Customer.find_by_id(customer_id)
        if customer:
            total_rental_amount = customer.calculate_total_rental_amount()
            print(f"Total Rental Amount: {total_rental_amount}")
        else:
            print("Customer not found.")
    except ValueError as e:
        print(str(e))

def display_main_menu():
    print("\nMain Menu:")
    print("1. Customer Menu")
    print("2. Car Store Menu")
    print("3. Rental Menu")
    print("4. Exit")

def main():
    while True:
        display_main_menu()
        try:
            choice = click.prompt("Enter your choice", type=int)
            if choice == 1:
                customer_menu()
            elif choice== 2:
                car_store_menu()
            elif choice == 3:
                rental_menu()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                raise ValueError("Invalid choice. Please try again.")
        except ValueError as e:
            print(str(e))

if __name__ == '__main__':
    main()