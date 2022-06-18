# Import your libraries
import pandas as pd

# Start writing code
employee = employee.groupby(["department"])["salary"].median()

employee.reset_index()