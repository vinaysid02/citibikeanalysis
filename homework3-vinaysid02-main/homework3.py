import pandas as pd
import numpy as nm
def countTrips(df):
    num_trips=len(df)
    return num_trips

def avgTripDuration(df):
    if 'tripduration' in df.columns:
        average_duration = df['tripduration'].mean()
        return average_duration
    
def maxTripDuration(year,df):
    if 'tripduration' in df.columns and 'birth year' in df.columns:
        filtered_df = df[(df['usertype'] == 'Subscriber') & (df['birth year'] >= year)]
        if not filtered_df.empty:
            max_duration = filtered_df['tripduration'].max()
            return max_duration
        else:
            return None
    else:
        return None


def countBikes(df):
    distinct_bikes = df['bikeid'].nunique()
    return distinct_bikes

def countStartStations(df):
    unique_station = df['start station id'].nunique()
    return unique_station


def countAllStations(df):
  #  unique_start_station = df['start station id'].nunique()
   # unique_end_station   = df['end station id'].nunique()
  #  all_stations = unique_start_station + unique_end_station
    unique_stations = set(df['start station id']).union(df['end station id'])
    # Calculate the number of unique stations
    total_unique_stations = len(unique_stations)
    return total_unique_stations

def avgTripsPerBike(df):
    trips_per_bike = df.groupby('bikeid')['tripduration'].count()
    avg_trip_per_bike =  trips_per_bike.mean()  
    return avg_trip_per_bike

def avgRiderAge(input_year, df):
    # Calculate the age of each rider based on the birth year (YYYY format)
    df['Birth_Year'] = pd.to_numeric(df['birth year'], errors='coerce')  # Convert to numeric, treat errors as NaN
    df['Age'] = input_year - df['Birth_Year']

    # Remove rows with missing birth year (NaN)
    df_new = df.dropna(subset=['Age'])

    # Calculate the average age of all riders
    average_age = df_new['Age'].mean()
    return average_age

def avgTripsByDayOfWeek(df):
    # Convert the 'Start Date' column to datetime to work with dates
    df['Start Date'] = pd.to_datetime(df['starttime'])
    
    # Extract the day of the week (0 = Monday, 6 = Sunday)
    df['Day of Week'] = df['Start Date'].dt.dayofweek

    # Group the data by day of the week and calculate the average number of trips
    avg_trips_by_day = df.groupby('Day of Week')['bikeid'].count()
    
    
    result = avg_trips_by_day.tolist()
    print('the result is ',result)
    result = result[6:] + result[:6]
    return result

def topXdepartures(x, bike_trip_dataframe):
    
    if not isinstance(bike_trip_dataframe, pd.DataFrame):
        raise ValueError("Input is not a pandas DataFrame")

    
    if 'start station id' not in bike_trip_dataframe.columns:
        raise ValueError("DataFrame must have a 'start station id' column")

    
    station_departures = bike_trip_dataframe.groupby('start station id').size().reset_index(name='number of departures')

    
    station_departures = station_departures.sort_values(by='number of departures', ascending=False)

   
    station_departures['rank'] = station_departures['number of departures'].rank(method='min', ascending=False).astype(int)

    
    top_x_stations = station_departures.head(x)
    
    top_x_stations = top_x_stations.reset_index(drop=True)

    return top_x_stations[['rank', 'start station id', 'number of departures']]


def numEarlyTrips(bike_trip_dataframe):
    # Check if the input is a pandas DataFrame
    if not isinstance(bike_trip_dataframe, pd.DataFrame):
        raise ValueError("Input is not a pandas DataFrame")
    if 'starttime' not in bike_trip_dataframe.columns:
        raise ValueError("DataFrame must have a 'starttime' column")
    bike_trip_dataframe['starttime'] = pd.to_datetime(bike_trip_dataframe['starttime'])
    early_trips = bike_trip_dataframe[(bike_trip_dataframe['starttime'].dt.hour >= 8) & (bike_trip_dataframe['starttime'].dt.hour < 10)]
    num_early_trips = len(early_trips)
    return num_early_trips