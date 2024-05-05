import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load datasets
df_calendar_dates = pd.read_csv('calendar_dates.txt', parse_dates=['date'], dayfirst=False)
df_trips = pd.read_csv('trips.txt')

# Merge the calendar_dates with trips to link trips with their dates
df_trips = df_trips.merge(df_calendar_dates, on='service_id', how='left')

# Check for missing dates and drop rows if necessary
df_trips.dropna(subset=['date'], inplace=True)

# Convert date column to datetime if not already
df_trips['date'] = pd.to_datetime(df_trips['date'], format='%Y%m%d', errors='coerce')

# Set date as index
df_trips.set_index('date', inplace=True)

# Count the number of trips per day
daily_trips = df_trips.groupby(df_trips.index).size()

# Split the data into training and testing sets
train_end = daily_trips.index[-31]  # last 30 days for testing
train_data = daily_trips[:train_end]
test_data = daily_trips[train_end:]

# Fit the SARIMAX model on the training data
model = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Predict on the test data
predictions = results.get_prediction(start=test_data.index[0], end=test_data.index[-1])
predictions_mean = predictions.predicted_mean

# Forecast beyond the available data
forecast = results.get_forecast(steps=30)
forecast_mean = forecast.predicted_mean

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(train_data.index, train_data, label='Train Data')
plt.plot(test_data.index, test_data, label='Test Data', color='orange')
plt.plot(predictions_mean.index, predictions_mean, label='Predictions', color='green')
plt.plot(forecast_mean.index, forecast_mean, label='30-day Forecast', color='red')
plt.title('Daily Trips Forecast')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.legend()
plt.show()
