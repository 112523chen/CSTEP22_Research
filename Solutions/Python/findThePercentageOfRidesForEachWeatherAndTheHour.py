import numpy
import pandas
lyft_rides = lyft_rides.groupby(["weather", "hour"])
lyft_rides = lyft_rides["index"].count()/len(lyft_rides)
lyft_rides.sort_values(ascending=True)
lyft_rides.reset_index()