# Electric-Vehicle-Charging-Infrastructure-Database
Part A
The scope is project is to keep track of how often certain electric vehicle charging stations are being used and where does charging stations are. This will help people who build or fund electric cars and their charging stations because it can help them determine want kind of places that should install more chargin stations
Data Source:https://www.kaggle.com/datasets/sahirmaharajj/electric-vehicle-charging-stations-2024
Part B
I plan to use 5 main entities in may database. These entities are Charging_Station, which will be used to store data regarding each specific stations, Charger, which will be used to catalog each type of charger each station has, EV_USER, which will store the data regarding each user of the stations, Charging-Session, which is an associative entitiy between Charger and EV_USER showing the stats of each time a user use a specific charger at a specific station, and Station_Performance_Index, which will store data related to how effective each station is.
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/9ac617a4fc15a7bbb72257ad8007f7635d598df8/Screenshot%202026-02-20%20101455.png
User Groups: Companys and constructions groups wanting to determine where it would be good to put charging stations for electric cars.
Part C
Charging_Station:
StationID	StationName	Address	City	State	ZipCode	Latitude	Longtitude
S101	Downtown FastCharge	123 Main St	Miami	FL	33101	25.76	-80.19
S102	Beachside EV Hub	456 Ocean Dr	Miami	FL	33139	25.79	-80.13
S103	Airport ChargePoint	2100 NW 42nd Ave	Miami	FL	33126	25.80	-80.29
InstallationDate	StationStatus	OperatorNote
03/10/2022	Active	Near mall
01/15/2023	Active	-
07/20/2021	Maintenance	Upgrading Unit
Charger:
StationID	ChagerNumber	ChagerType	MaxPowerKW	Status	LastMaintenanceDate
S101	1	DC Fast	150	Available	01/10/2025
S101	2	Level 2	50	In Use	01/02/2025
S102	1	DC Fast	120	Available	01/22/2025
EV_USER:
UserID	FirstName	LastName	Email	PhoneNumber	MembershipType RegistrationDate
U001	Tyler	Smith	tyler@email.com 305-555-1111	Premium 01/05/2024
U002	Maria	Lopez	maria@email.com 305-555-2222	Standard 06/15/2024
U003	James	Carter	james@email.com	NULL	Premium 01/10/2025
Charging_Session:
SessionID	UserID	StationID	ChagerNumber	StartTime	EndTime
SS001	U001	S101	1	01/03/2025 10:00	01/03/2025 10:45
SS002	U002	S101	2	01/03/2025 11:00	01/03/2025 12:30
SS003	U003	S102	1	02/03/2025 09:15	NULL
EnergyConsumedKWh	TotalCost	SessionStatus	PaymentMethod
35	14.00	Completed	Credit Card
20	8.00	Completed	Mobile App
10	4.00	Active	Credit Card
Station_Performance_Index:
StationID UtilizationRate	AvailabilityPercentage	AvgSessionDuration	RevenuePerDay
S101 0.78	82	52	450.00
S102 0.64 88	48	320.00
S103 0.55	91	40	210.00
UtilizationRank:
UtilizationRate	UtilizationRank
0.78	1
0.64	2
0.55	3
