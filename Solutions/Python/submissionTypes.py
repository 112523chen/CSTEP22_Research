# Import your libraries
import pandas as pd

# Start writing code
loans.head()

loans_a = loans[(loans.type == 'Refinance')]
loans_b = loans[(loans.type == 'InSchool')]
loans = loans_a.merge(loans_b, on='user_id', how='inner')
loans['user_id'].unique()