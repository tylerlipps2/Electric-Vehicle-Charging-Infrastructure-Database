import streamlit as st
import pandas as pd
import oracledb

oracledb.init_oracle_client(
    lib_dir=r"C:\Users\tyler\Downloads\instantclient_23_0")

username = "TYLERLIPPS2_SCHEMA_UEH5S"
password = "IAK57N025Z6!PVZFBW5YRDKL3AsQR2"
dsn = "db.freesql.com:1521/23ai_34ui2"

def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)

def run_query(query, params=None):
    connection = get_connection()
    df = pd.read_sql(query, connection, params=params)
    connection.close()
    return df

st.title("EV Charging Dashboard")
st.sidebar.header("Menu")
option = st.sidebar.selectbox(
    "Choose a feature", [
        "1. Charging Sessions",
        "2. Search Stations",
        "3. Charger Types",
        "4. Station Performance",
        "5. View Users",
    ])

if option == "1. Charging Sessions":
    st.header("Charging Sessions History")
    user_id = st.text_input("Enter User ID")

    if st.button("Get Charging Sessions"):
        query = """
        SELECT *
        FROM Charging_Session
        WHERE User_ID = :1
        """
        df = run_query(query, [user_id])
        if df.empty:
            st.warning("No Charging Sessions found")
        else:
            st.dataframe(df)
elif option == "2. Search Stations":
    st.header("Search Stations by City")
    city = st.text_input("Enter City")
    if st.button("Get Search Stations"):
        query = """
        SELECT
            cs.Station_ID,
            cs.Station_Name,
            cs.Station_Address,
            cs.City,
            c.Charger_Number,
            c.Charger_Type,
            c.Max_Power_KW
        FROM Charging_Station cs
        LEFT JOIN Charger c
            ON cs.Station_ID = c.Station_ID
        WHERE LOWER(cs.city) = LOWER(:1)
        """
        df = run_query(query, [city])
        if df.empty:
            st.warning("No Charging Sessions found")
        else:
            st.dataframe(df)
elif option == "3. Charger Types":
    st.header("Charger Types with Station Info")
    query = """
    SELECT 
        cs.Station_Name,
        cs.Station_Address,
        cs.City,
        c.Charger_Number,
        c.Charger_Type,
        c.Max_Power_KW
    FROM Charger c
    JOIN Charging_Station cs 
        ON cs.Station_ID = c.Station_ID
    """
    df = run_query(query)
    if df.empty:
        st.warning("No Charging Types found")
    else:
        st.dataframe(df)
elif option == "4. Station Performance":
    st.header("Station Performance")
    query = """
    SELECT Station_ID, Revenue_Per_Day, Utilization_Rate, Utilization_Rank
    FROM Station_Performance_Index
    """
    df = run_query(query)
    if df.empty:
        st.warning("No Station Performance found")
    else:
        st.dataframe(df)
elif option == "5. View Users":
    st.header("View Users")
    query = """
    SELECT * FROM EV_User
    """
    df = run_query(query)
    if df.empty:
        st.warning("No User found")
    else:
        st.dataframe(df)