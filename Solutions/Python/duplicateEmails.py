# Import your libraries
import pandas as pd

# Start writing code
employee['dup'] = employee.duplicated(subset=['email'])
employee[employee.dup == True]['email'].unique()
