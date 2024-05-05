import pandas as pd

# Load the datasets
agency = pd.read_csv('agency.txt')
calendar_dates = pd.read_csv('calendar_dates.txt')
calendar = pd.read_csv('calendar.txt')
pathways = pd.read_csv('pathways.txt')
routes = pd.read_csv('routes.txt')
stop_times = pd.read_csv('stop_times.txt')
stops = pd.read_csv('stops.txt')
transfers = pd.read_csv('transfers.txt')
trips = pd.read_csv('trips.txt')

# Check the first few rows of each DataFrame to understand the data
print(agency.head())
print(calendar_dates.head())
print(calendar.head())
print(pathways.head())
print(routes.head())
print(stop_times.head())
print(stops.head())
print(transfers.head())
print(trips.head())

# Basic info about each DataFrame to understand the types and non-null counts
agency.info()
calendar_dates.info()
calendar.info()
pathways.info()
routes.info()
stop_times.info()
stops.info()
transfers.info()
trips.info()

print(f"Unique routes: {routes['route_id'].nunique()}")
print(f"Unique stops: {stops['stop_id'].nunique()}")
print(f"Unique trips: {trips['trip_id'].nunique()}")


stops_per_trip = stop_times.groupby('trip_id').size()
print(stops_per_trip.describe())

# Visualizations in EDA
import matplotlib.pyplot as plt

# Plotting the distribution of stops per trip
stops_per_trip.hist(bins=50)
plt.title('Distribution of Stops per Trip')
plt.xlabel('Number of Stops')
plt.ylabel('Frequency')
plt.show()
