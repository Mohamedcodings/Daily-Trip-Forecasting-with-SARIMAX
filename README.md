
# Trip Forecasting Project

## Project Overview

This project focuses on forecasting the number of daily trips using public transit data. The datasets include detailed information about calendar dates, trips, stops, and more. The main objectives are:

- **Data Exploration**: Understanding the data distribution and relationships using exploratory data analysis.
- **Forecasting**: Using a SARIMAX model to predict future trips.

## Project Structure

- **data_exploration.py**: Contains code for exploring the data, including summary statistics and visualizations.
- **trip_forecasting.py**: Implements the SARIMAX model to forecast daily trips, visualizing historical data, predictions, and future forecasts.
- **forecast1.png**: Graph showing the historical data, predictions, and 30-day forecast of daily trips.
- **forecast2.png**: Histogram visualizing the distribution of stops per trip.

## Data Sources

- **agency.txt**: Contains information about transit agencies.
- **calendar.txt**: Service availability by day of the week.
- **calendar_dates.txt**: Special dates and attributes like holidays.
- **routes.txt**: Information about different transit routes.
- **stop_times.txt**: Contains the stop times for each trip.
- **stops.txt**: Details about transit stops.
- **transfers.txt**: Information about transfers between stops.
- **trips.txt**: Trip details, linked to dates via `service_id`.

## Usage

### Prerequisites
- Python 3.x
- Install required packages: `pandas`, `matplotlib`, `statsmodels`

### Instructions
1. **Clone the Repository**: `git clone <repo_url>`
2. **Install Dependencies**: Run `pip install -r requirements.txt` if a requirements file is present, or install packages manually.
3. **Run the Scripts**:
   - For data exploration, execute `python data_exploration.py`.
   - For trip forecasting, execute `python trip_forecasting.py`.
4. **View Outputs**: Results are saved as images (`forecast1.png` and `forecast2.png`).

### Sample Outputs
- `forecast1.png`: Displays historical trips, predictions, and forecasts.
- `forecast2.png`: Shows a histogram of stops per trip.

## Conclusion

This project demonstrates the use of time series analysis for trip forecasting and provides insights into the data structure. Adjustments to the model and parameters can enhance forecasting accuracy.
