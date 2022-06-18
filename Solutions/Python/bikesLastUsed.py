# Import your libraries
import pandas as pd

# Start writing code
df = dc_bikeshare_q1_2012.groupby(['bike_number'])['end_time'].max()
df.sort_values(ascending=False).reset_index()