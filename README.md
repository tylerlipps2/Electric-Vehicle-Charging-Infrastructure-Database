# Electric-Vehicle-Charging-Infrastructure-Database
Part A
The scope is project is to keep track of how often certain electric vehicle charging stations are being used and where does charging stations are. This will help people who build or fund electric cars and their charging stations because it can help them determine want kind of places that should install more chargin stations
Data Source:https://www.kaggle.com/datasets/sahirmaharajj/electric-vehicle-charging-stations-2024
Part B
I plan to use 5 main entities in may database. These entities are Charging_Station, which will be used to store data regarding each specific stations, Charger, which will be used to catalog each type of charger each station has, EV_USER, which will store the data regarding each user of the stations, Charging-Session, which is an associative entitiy between Charger and EV_USER showing the stats of each time a user use a specific charger at a specific station, and Station_Performance_Index, which will store data related to how effective each station is.
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/9ac617a4fc15a7bbb72257ad8007f7635d598df8/Screenshot%202026-02-20%20101455.png
User Groups: Companys and constructions groups wanting to determine where it would be good to put charging stations for electric cars.
Part C
ER:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/Database%201%20Project%20C%20image.png
Doc:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/Database%201%20Project%20C.docx
Part D
ER:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/Database%201%20Project%20D%20ER.png
SQL:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/create_db.sql
Unfiltered CSV:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/Database%201%20Project%20D%20CSV.csv
Preprocess:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/preprocess.py
Filtered CSV's:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/ChargingStation.csv
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/Charger.csv
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/EVUser.csv
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/ChargingSession.csv
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/StationPerformanceIndex_df.csv
Dataload:
https://github.com/tylerlipps2/Electric-Vehicle-Charging-Infrastructure-Database/blob/main/dataload.py
