import pandas as pd

input_file = "Database 1 Project D CSV.csv"

df = pd.read_csv(input_file)

chargingStation_df = df[["Station_ID", "StationName", "StationAddress", "City"]].drop_duplicates().copy()
charger_df = df[["Station_ID", "ChargerNumber", "ChargerTyper", "MaxPowerKW"]].drop_duplicates().copy()
evUser_df = df[["UserID", "FirstName", "LastName", "PhoneNumber"]].drop_duplicates().copy()
chargingSession_df = df[["ChargeSessionID", "UserID", "Station_ID",
                        "ChargerNumber", "ChargeStartTime", "ChargeEndTime", "EnergyConsumedKWh", "TotalCost"]].drop_duplicates().copy()
stationPerformanceIndex_df = df[["Station_ID", "Availability", "AvgSessionDurration", "RevenuePerDay",
                                 "UtilizationRate", "UtilizationRank"]].drop_duplicates().copy()

chargingStation_df.to_csv("ChargingStation.csv", index=False)
charger_df.to_csv("Charger.csv", index=False)
evUser_df.to_csv("EVUser.csv", index=False)
chargingSession_df.to_csv("ChargingSession.csv", index=False)
stationPerformanceIndex_df.to_csv("StationPerformanceIndex_df.csv", index=False)