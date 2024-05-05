import csv
import sqlite3

def create_db():
    # If the db does not exist this command will create the file
    conn = sqlite3.connect('database.db')

    # Cursor to execute SQL commands
    cursor = conn.cursor()

    # We create the table, later more columns can be added
    cursor.execute('''CREATE TABLE Info (
                    TripID INTEGER PRIMARY KEY,
                    TravellerName TEXT,
                    DepartureDate TEXT,
                    ReturnDate TEXT,
                    DepartureCity TEXT,
                    ArrivalCity TEXT,
                    Sport TEXT
                    )''')

    # We save the changes and close the connection
    conn.commit()
    conn.close()

def insert_data_from_csv(csv_file):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            trip_id = row['Trip ID']
            traveller_name = row['Traveller Name']
            departure_date = row['Departure Date']
            return_date = row['Return Date']
            departure_city = row['Departure City']
            arrival_city = row['Arrival City']
            sport = row['Sport']

            cursor.execute('''INSERT INTO Info
                              (TripID, TravellerName, DepartureDate, ReturnDate, DepartureCity, ArrivalCity, Sport) 
                              VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (trip_id, traveller_name, departure_date, return_date, departure_city, arrival_city, sport))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
    insert_data_from_csv('dataset.csv')
