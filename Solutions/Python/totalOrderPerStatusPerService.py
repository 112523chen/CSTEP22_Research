# Import your libraries
import pandas as pd

# Start writing code
uber_orders.head()
df = uber_orders.groupby(['service_name', 'status_of_order']).sum()
df = df['number_of_orders'].reset_index()
df