# import sqlite3

# CONN = sqlite3.connect('main.db')
# CURSOR = CONN.cursor()

# def insert_sample_customers():
#     customers = [
#         ("John Doe", 1, 3),
#         ("Jane Smith", 2, 7),
#         ("Alice Johnson", 1, 5),
#     ]

#     for customer in customers:
#         CURSOR.execute("INSERT INTO customers (name, rent_type, rent_period) VALUES (?, ?, ?)", customer)

#     CONN.commit()

# def insert_sample_car_stores():
#     car_stores = [
#         (1, "sedan", 10, 50),
#         (2, "suv", 5, 70),
#         (3, "truck", 8, 60),
#     ]

#     for car_store in car_stores:
#         CURSOR.execute("INSERT INTO car_stores (store_id, car_type, number_of_cars, hourly_rental_rate) VALUES (?, ?, ?, ?)", car_store)

#     CONN.commit()

# def insert_sample_rentals():
#     rentals = [
#         (1, 1, 1, 1, "2022-01-01", "2022-01-03"),
#         (2, 2, 2, 2, "2022-01-05", "2022-01-07"),
#         (3, 3, 3, 3, "2022-01-09", "2022-01-10"),
#     ]

#     for rental in rentals:
#         CURSOR.execute("INSERT INTO rentals (rental_id, customer_id, store_id, car_id, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)", rental)

#     CONN.commit()

# if __name__ == "__main__":
#     insert_sample_customers()
#     insert_sample_car_stores()
#     insert_sample_rentals()