import sqlite3
from datetime import datetime as dt, timedelta
from sports_api_queries import *
import pprint

countries = {"Amsterdam":"The Netherlands", "Atenas":"Greece", "Barcelona":"Spain", "Berlin":"Germany",
        "Bratislava":"Germany", "Bruselas":"Belgium", "Budapest":"Hungary", "Copenhague":"Denmark",
        "Dublin":"Ireland", "Dubrovnik":"Croatia", "Edimburgo":"Scotland", "Estocolmo":"Sweden",
        "Franckfurt":"Germany","Helsinki":"Finland", "Lisboa":"Portugal", "Londres":"United Kingdom",
        "Lyon":"France", "Madrid":"Spain", "Milan":"Italy", "Moscu":"Russian Federation", 
        "Munich":"Germany", "Niza":"France", "Oslo":"Norway", "Paris":"France", "Praga":"Czech Republic",
        "Roma":"Italy", "Varsovia":"Poland", "Venecia":"Italy", "Viena":"Austria", "Zurich":"Sweden"}

def parseDate(date):
    return dt.strptime(date, "%d/%m/%Y")


def insert_travel(traveller_name, departure_date, return_date, departure_city, arrival_city, sport):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # We compute the new TripID
    cursor.execute('''SELECT MAX(TripID) FROM Info''')
    last_trip_id = cursor.fetchone()[0]
    new_trip_id = last_trip_id + 1 if last_trip_id else 1

    print(departure_date, return_date)
   
    departure_date = dt.strptime(departure_date, "%Y-%m-%d").strftime("%d/%m/%Y")
    return_date = dt.strptime(return_date, "%Y-%m-%d").strftime("%d/%m/%Y")

    # We insert the new travel
    cursor.execute('''INSERT INTO Info
                      (TripID, TravellerName, DepartureDate, ReturnDate, DepartureCity, ArrivalCity, Sport) 
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (new_trip_id, traveller_name, departure_date, return_date, departure_city, arrival_city, sport))

    conn.commit()
    conn.close()
    
    # We return the new trip ID
    return new_trip_id

def matching_dates(ini1, ret1, ini2, ret2):
    dates = []

    for i in range((ret1 - ini1).days + 1):
        day = ini1 + timedelta(days=i)
        if ini2 <= day <= ret2:
            dates.append(day.strftime('%d/%m/%Y'))
    return dates


def get_user_data(trip_id):
    conn = sqlite3.connect('database.db');
    cursor = conn.cursor();

    cursor.execute('''SELECT * FROM Info WHERE TripID=?''', (trip_id,));

    traveler_data = cursor.fetchall()[0];

    conn.close();
    
    return traveler_data, 200;


def get_compatibles(trip_id, departure_date, return_date, departure_city, arrival_city,sport):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT TravellerName, DepartureDate, ReturnDate FROM Info
                      WHERE ArrivalCity = ? AND Sport = ? AND TripID <> ?''',
                      (arrival_city,sport, trip_id))

    travelers_same_arrival = cursor.fetchall()

    compatible_travelers = []
    departure = parseDate(departure_date)
    ret = parseDate(return_date)

    # For now we only search people in the same city in compatible days
    for traveler in travelers_same_arrival:
        t_departure = parseDate(traveler[1])
        t_return = parseDate(traveler[2])
    
        match_dates = matching_dates(departure, ret, t_departure, t_return)

        if len(match_dates) > 0:
            compatible_travelers.append((traveler[0], match_dates))
    
    conn.commit()
    conn.close()

    return compatible_travelers
    #return travelers_same_arrival

if __name__ == "__main__":
    # Example
    name = "Paco"
    date1 = '28/03/2024'
    date2 = '04/04/2024'
    city1 = "Barcelona"
    city2 = "Madrid"
    sport = "Soccer"

    #ident = insert_travel("Paco", date1, date2, city1, city2, sport)
    compatibles = get_compatibles(date1, date2, city1, city2, sport)

    country = countries[city2]
    
    compatibles = dict(compatibles)
    
    for key, values in compatibles.items():
        parsedDates = [parseDate(s) for s in values]
        compatibles[key] = parsedDates

    print(compatibles)

    resultado = obtener_personas_y_eventos(country, sport, parseDate(date1), parseDate(date2), compatibles)

    pprint.pprint(resultado)


