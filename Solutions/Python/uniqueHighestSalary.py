import numpy
import pandas

employee.drop_duplicates(subset=['salary'])
employee.sort_values('salary', inplace=True, ascending=False)
employee.salary.head(1)