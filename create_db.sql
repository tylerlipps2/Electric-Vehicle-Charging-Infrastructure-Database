Create Table Charging_Station (
    Station_ID varchar2(10),
    Station_Name varchar2(100) NOT NULL,
    Station_Address VARCHAR2(100) NOT NULL,
    City varchar2(100) NOT NULL,
    
    CONSTRAINT PK_Charging_Station Primary KEY
    (Station_ID)
);

Create Table Charger (
    Station_ID varchar2(10),
    Charger_Number varchar2(10),
    Charger_Type varchar2(20),
    Max_Power_KW number(20),

    CONSTRAINT PK_Charger Primary KEY
    (Station_ID, Charger_Number)

);

Create Table EV_User (
    User_ID varchar2(10),
    First_Name varchar2(50) NOT NULL,
    Last_Name varchar2(50) NOT NULL,
    Phone_Number varchar(30) UNIQUE NOT NULL,

    CONSTRAINT PK_EV_User Primary KEY
    (User_ID)
);

Create Table Charging_Session(
    Charge_Session_ID varchar2(10),
    User_ID varchar2(10) NOT NULL,
    Station_ID varchar2(10) NOT NULL,
    Charger_Number varchar2(10) NOT NULL,
    Charge_Start_Time TIMESTAMP(30),
    Charge_End_Time TIMESTAMP(30),
    Energy_Consumed_KWh DECIMAL(10,2),
    Total_Cost DECIMAL(10,2),

    CONSTRAINT PK_Chargin_Station Primary KEY
    (Charge_Session_ID)
);

Create Table Station_Performance_Index (
    Station_ID varchar2(10),
    Availability varchar2(100),
    Avg_Session_Duriation DECIMAL(10,2),
    Revenue_Per_Day DECIMAL(10,2),
    Utilization_Rate DECIMAL(10,2),
    Utilization_Rank number(20),

    CONSTRAINT PK_Station_Performance_Index Primary KEY
    (Station_ID)
);

Alter Table Charger
Add Constraint FK_Charger_Station
Foreign Key(Station_ID)
References Charging_Station(Station_ID);

Alter Table Charging_Session
Add Constraint FK_Session_User
Foreign Key(User_ID)
References EV_User(User_ID);

Alter Table Charging_Session
Add Constraint FK_Session_Charger
Foreign Key(Station_ID, Charger_Number)
References Charger(Station_ID, Charger_Number);

Alter Table Station_Performance_Index
Add Constraint FK_Performance_Station
Foreign Key(Station_ID)
References Charging_Station(Station_ID);