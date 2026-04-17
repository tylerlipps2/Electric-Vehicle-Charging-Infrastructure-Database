import pandas as pd
import sqlite3

# ---------------- SETUP DATABASE ----------------
conn = sqlite3.connect("ev.db")

charging_session = pd.read_csv("ChargingSession.csv")
charging_station = pd.read_csv("ChargingStation.csv")
ev_user = pd.read_csv("EVUser.csv")
station_perf = pd.read_csv("StationPerformanceIndex_df.csv")
charger = pd.read_csv("Charger.csv")

charging_session.to_sql("ChargingSession", conn, if_exists="replace", index=False)
charging_station.to_sql("ChargingStation", conn, if_exists="replace", index=False)
ev_user.to_sql("EVUser", conn, if_exists="replace", index=False)
station_perf.to_sql("StationPerformanceIndex", conn, if_exists="replace", index=False)
charger.to_sql("Charger", conn, if_exists="replace", index=False)

cursor = conn.cursor()

# ---------------- FUNCTIONS ----------------

def view_charging_sessions(cursor, is_admin, user_id):
    print("\n--- Charging Session History ---\n")

    if is_admin:
        search_id = input("Enter UserID to view history: ").strip()
    else:
        search_id = user_id

    cursor.execute("""
        SELECT *
        FROM ChargingSession
        WHERE UserID = ?
    """, (search_id,))

    rows = cursor.fetchall()

    if not rows:
        print("None found in dataset.")
        return

    headers = [desc[0] for desc in cursor.description]
    print(" | ".join(headers))
    print("-" * 80)

    for row in rows:
        print(" | ".join(map(str, row)))


def search_stations_by_city(cursor):
    print("\n--- Search Charging Stations by City ---\n")

    city = input("Enter city: ").strip().lower()

    cursor.execute("""
        SELECT 
            cs.Station_ID,
            cs.StationName,
            cs.StationAddress,
            cs.City,
            c.ChargerNumber,
            c.ChargerTyper,
            c.MaxPowerKW
        FROM ChargingStation cs
        LEFT JOIN Charger c
            ON cs.Station_ID = c.Station_ID
        WHERE LOWER(cs.City) = ?
    """, (city,))

    rows = cursor.fetchall()

    if not rows:
        print("None found in dataset.")
        return

    headers = [desc[0] for desc in cursor.description]
    print(" | ".join(headers))
    print("-" * 80)

    for r in rows:
        print(" | ".join(map(str, r)))


def view_station_performance(cursor):
    print("\n--- Station Performance Index ---\n")

    cursor.execute("""
        SELECT Station_ID, RevenuePerDay, UtilizationRate, UtilizationRank
        FROM StationPerformanceIndex
    """)

    rows = cursor.fetchall()

    if not rows:
        print("None found in dataset.")
        return

    headers = [desc[0] for desc in cursor.description]
    print(" | ".join(headers))
    print("-" * 80)

    for r in rows:
        print(" | ".join(map(str, r)))


def view_charger_types(cursor):
    print("\n--- Charger Types with Station Info ---\n")

    cursor.execute("""
        SELECT 
            cs.StationName,
            cs.StationAddress,
            cs.City,
            c.ChargerNumber,
            c.ChargerTyper,
            c.MaxPowerKW
        FROM Charger c
        JOIN ChargingStation cs
            ON c.Station_ID = cs.Station_ID
    """)

    rows = cursor.fetchall()

    if not rows:
        print("None found in dataset.")
        return

    headers = [desc[0] for desc in cursor.description]
    print(" | ".join(headers))
    print("-" * 100)

    for r in rows:
        print(" | ".join(map(str, r)))


# ---------------- LOGIN ----------------
print("=== EV USER LOGIN ===")

user_id = input("UserID [UXXX]: ").strip()
first_name = input("First Name: ").strip()
last_name = input("Last Name: ").strip()
phone = input("Phone Number [XXX-XXX-XXXX]: ").strip()

cursor.execute("""
    SELECT *
    FROM EVUser
    WHERE UserID = ?
    AND FirstName = ?
    AND LastName = ?
    AND PhoneNumber = ?
""", (user_id, first_name, last_name, phone))

user = cursor.fetchone()

is_admin = (
    user_id == "A000"
    and first_name.upper() == "ADMIN"
    and last_name.upper() == "ADMIN"
    and phone == ""
)

# ---------------- APP LOGIC ----------------

if user or is_admin:

    if is_admin:
        print("\nADMIN LOGIN SUCCESSFUL\n")
    else:
        print("\nLogin successful!\n")

    while True:

        if is_admin:
            prompt = input("""
ADMIN MENU:
1. View Charging Session History
2. Search Charging Stations by City
3. View Charger Types
4. View Station Performance Index (ADMIN ONLY)
5. View All Users
6. Logout

Select option [1-6]: """)
        else:
            prompt = input("""
USER MENU:
1. View Charging Session History
2. Search Charging Stations by City
3. View Charger Types
4. Logout

Select option [1-4]: """)

        if prompt == "1":
            view_charging_sessions(cursor, is_admin, user_id)

        elif prompt == "2":
            search_stations_by_city(cursor)

        elif prompt == "3":
            view_charger_types(cursor)

        elif prompt == "4" and is_admin:
            view_station_performance(cursor)

        elif prompt == "5" and is_admin:
            cursor.execute("SELECT * FROM EVUser")
            rows = cursor.fetchall()

            if not rows:
                print("None found in dataset.")
            else:
                headers = [desc[0] for desc in cursor.description]
                print("\n | ".join(headers))
                print("-" * 80)

                for r in rows:
                    print(" | ".join(map(str, r)))

        elif (prompt == "4" and not is_admin) or (prompt == "6" and is_admin):
            print("Logging out...")
            break

        else:
            print("Invalid option")

conn.close()