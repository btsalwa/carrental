import sqlite3

CONN = sqlite3.connect('main.db')
CURSOR = CONN.cursor()

class Customer:
    def __init__(self, customer_id, name, rent_type, rent_period):
        self.customer_id = customer_id
        self.name = name
        self.rent_type = rent_type
        self.rent_period = rent_period

    def save(self):
        CURSOR.execute("INSERT INTO customers (name, rent_type, rent_period) VALUES (?, ?, ?)",
                        (self.name, self.rent_type, self.rent_period))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM customers WHERE name=?", (self.name,))
        CONN.commit()

    @staticmethod
    def get_all():
        CURSOR.execute("SELECT * FROM customers")
        customer_data = CURSOR.fetchall()
        customers = [Customer(*row) for row in customer_data]
        return customers

    @staticmethod
    def find_by_id(customer_id):
        CURSOR.execute("SELECT * FROM customers WHERE customer_id=?", (customer_id,))
        customer_data = CURSOR.fetchone()
        if customer_data:
            return Customer(*customer_data)
        return None

    def show_cars(self):
        # Implement this method to show cars related to the customer
        pass

    @classmethod
    def ensure_table_exists(cls):
        try:
            cls.create_table()
        except sqlite3.OperationalError as e:
            if "table customers already exists" not in str(e):
                raise

    @classmethod
    def create_table(cls):
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS customers (
                            customer_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            rent_type INTEGER NOT NULL,
                            rent_period INTEGER NOT NULL
                        )""")
        CONN.commit()

class CarStore:
    def __init__(self, store_id, car_type, number_of_cars, hourly_rental_rate):
        self.store_id = store_id
        self.car_type = car_type
        self.number_of_cars = number_of_cars
        self.hourly_rental_rate = hourly_rental_rate

    def save(self):
        CURSOR.execute("INSERT INTO car_stores (store_id, car_type, number_of_cars, hourly_rental_rate) VALUES (?, ?, ?, ?)",
                        (self.store_id, self.car_type, self.number_of_cars, self.hourly_rental_rate))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM car_stores WHERE store_id=?", (self.store_id,))
        CONN.commit()

    @staticmethod
    def get_all():
        CURSOR.execute("SELECT * FROM car_stores")
        car_store_data = CURSOR.fetchall()
        car_stores = [CarStore(*row) for row in car_store_data]
        return car_stores

    @staticmethod
    def find_by_id(store_id):
        CURSOR.execute("SELECT * FROM car_stores WHERE store_id=?", (store_id,))
        car_store_data = CURSOR.fetchone()
        if car_store_data:
            return CarStore(car_store_data[0], car_store_data[1], car_store_data[2], car_store_data[3])
        return None

    def show_cars(self):
        # Implement this method to show cars related to the car store
        pass

    @classmethod
    def create_table(cls):
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS car_stores (
                            store_id INTEGER PRIMARY KEY,
                car_type TEXT NOT NULL,
                            number_of_cars INTEGER NOT NULL,
                            hourly_rental_rate REAL NOT NULL
                        )""")
        CONN.commit()

class Rental:
    def __init__(self, rental_id, customer_id, store_id, car_id, start_date, end_date):
        self.rental_id = rental_id
        self.customer_id = customer_id
        self.store_id = store_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date

    def save(self):
        CURSOR.execute("INSERT INTO rentals (rental_id, customer_id, store_id, car_id, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)",
                        (self.rental_id, self.customer_id, self.store_id, self.car_id, self.start_date, self.end_date))
        CONN.commit()

    def delete(self):
        CURSOR.execute("DELETE FROM rentals WHERE rental_id=?", (self.rental_id,))
        CONN.commit()

    @staticmethod
    def get_all():
        CURSOR.execute("SELECT * FROM rentals")
        rental_data = CURSOR.fetchall()
        rentals = [Rental(*row) for row in rental_data]
        return rentals

    @staticmethod
    def find_by_id(rental_id):
        CURSOR.execute("SELECT * FROM rentals WHERE rental_id=?", (rental_id,))
        rental_data = CURSOR.fetchone()
        if rental_data:
            return Rental(rental_data[0], rental_data[1], rental_data[2], rental_data[3], rental_data[4], rental_data[5])
        return None

    @classmethod
    def create_table(cls):
        CURSOR.execute("""CREATE TABLE IF NOT EXISTS rentals (
                            rental_id TEXT PRIMARY KEY,
                            customer_id INTEGER,
                            store_id INTEGER,
                            car_id INTEGER,
                            start_date TEXT,
                            end_date TEXT
                        )""")
        CONN.commit()

if __name__ == "__main__":
    Customer.create_table() 
    CarStore.create_table()
    Rental.create_table()