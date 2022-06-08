import pandas as pd

data = pd.read_csv('data.csv')

current_columns = (list(data.columns))
new_column_order = ['file', 'company_name', 'title', 'question_type', 'python_difficulty',
                    'mySQL_difficulty', 'postgreSQL_difficulty', 'prompt', 'source', 'question_id']

df = data[new_column_order]

df.to_csv('data_.csv', index=False)
