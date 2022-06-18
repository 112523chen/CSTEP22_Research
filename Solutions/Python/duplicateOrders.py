# Import your libraries
import pandas as pd

# Start writing code
orders['dup_cust_id'] = orders.groupby(
    ['cust_id'])['cust_id'].transform('count')
orders[orders.dup_cust_id > 3]['cust_id'].unique()
