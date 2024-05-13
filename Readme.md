Car Rental

This is a command-line interface (CLI) app that manages car rentals. It allows you to:

    Add, list, update, and delete customers
    Add, list, update, and delete car stores
    Rent and return cars from a car store
    List all rentals

Getting Started
 
    Install the required packages by running:

bash

pip install click

    Run the CLI app:

bash

python main.py run

    Follow the on-screen instructions to perform various operations.

Commands

    Add Customer: To add a new customer, use the command:

bash

add_customer <customer_id> <customer_name>

    List Customers: To list all customers, use the command:

bash

list_customers

    Update Customer: To update a customer's details, use the command:

bash

update_customer <customer_id> <new_customer_name>

    Delete Customer: To delete a customer, use the command:

bash

delete_customer <customer_id>

    Add Car Store: To add a new car store, use the command:

bash

add_car_store <store_id> <car_type> <number_of_cars> <hourly_rental_rate>

    List Car Stores: To list all car stores, use the command:

bash

list_car_stores

    Update Car Store: To update a car store's details, use the command:

bash

update_car_store <store_id> <new_car_type> <new_number_of_cars> <new_hourly_rental_rate>

    Delete Car Store: To delete a car store, use the command:

bash

delete_car_store <store_id>

    Rent Car: To rent a car from a car store, use the command:

bash

rent_car <rental_id> <customer_id> <store_id> <car_id> <start_date> <end_date>

    Return Car: To return a rented car, use the command:

bash

return_car <rental_id>

    List Rentals: To list all rentals, use the command:

bash

list_rentals