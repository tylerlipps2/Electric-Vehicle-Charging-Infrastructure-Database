import oracledb
import csv

# --- SETUP ---
LIB_DIR = r"C:\Users\tyler\Downloads\instantclient_23_0" # Your Instant Client Path
DB_USER = "TYLERLIPPS2_SCHEMA_UEH5S"
DB_PASS = "IAK57N025Z6!PVZFBW5YRDKL3AsQR2"
DB_DSN = "db.freesql.com:1521/23ai_34ui2"

# Initialize Thick Mode (Required for FreeSQL/Cloud)
oracledb.init_oracle_client(lib_dir=LIB_DIR)


def bulk_load_csv(file_path):
    try:
        # 1. Connect
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()

        # 2. Read CSV Data into a List
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            data_to_insert = [row for row in reader]

        # 3. Prepare Bulk Insert SQL
        # :1 and :2 correspond to the values in each row of your list
        if file_path == 'ChargingStation.csv':
            sql = "INSERT INTO Charging_Station (Station_ID, Station_Name, Station_Address, City) VALUES (:1, :2, :3, :4)"
        elif file_path == 'Charger.csv':
            sql = "INSERT INTO Charger (Station_ID, Charger_Number, Charger_Type, Max_Power_KW) VALUES (:1, :2, :3, :4)"
        elif file_path == 'EVUser.csv':
            sql = "INSERT INTO EV_User (User_ID, First_Name, Last_Name, Phone_Number) VALUES (:1, :2, :3, :4)"
        elif file_path == 'ChargingSession.csv':
            sql = ("""INSERT INTO Charging_Session (Charge_Session_ID, User_ID, Station_ID, Charger_Number, Charge_Start_Time, Charge_End_Time, Energy_Consumed_KWh, Total_Cost) VALUES (:1, :2, :3, :4, to_date(:5,'MM/DD/YYYY HH24:MI:SS'), to_date(:6, 'MM/DD/YYYY HH24:MI:SS'), :7, :8)""")
        elif file_path == 'StationPerformanceIndex_df.csv':
            sql = "INSERT INTO Station_Performance_Index (Station_ID, Availability, Avg_Session_Duriation, Revenue_Per_Day, Utilization_Rate, Utilization_Rank) VALUES (:1, :2, :3, :4, :5, :6)"


        # 4. Execute Batch
        print(f"Starting bulk load of {len(data_to_insert)} rows...")
        cursor.executemany(sql, data_to_insert)

        # 5. Commit Changes
        conn.commit()
        print(f"Successfully loaded {cursor.rowcount} rows into the database.")

    except Exception as e:
        print(f"Error during bulk load: {e}")
        if 'conn' in locals():
            conn.rollback()  # Undo changes if an error occurs

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()


# Run the function
bulk_load_csv('ChargingStation.csv')
bulk_load_csv('Charger.csv')
bulk_load_csv('EVUser.csv')
bulk_load_csv('ChargingSession.csv')
bulk_load_csv('StationPerformanceIndex_df.csv')