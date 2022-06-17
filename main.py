import ast
from st_aggrid import GridUpdateMode, DataReturnMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd

from Functions import getDatasetAsDataFrame
from Questions import Question
logic_df = pd.read_csv('data_.csv')


# stores nested dictionary
datasets_by_company = dict()

# sorts dataframe by companies
logic_by_company = logic_df.groupby("company_name")

# creates a list of unique company names
companies = list(logic_df["company_name"].unique())

# creates a list of unique question IDs
question_IDs = list(logic_df["question_id"].unique())

# creates a dictionary within another dictionary for referencing questions
for company in companies:
    if company not in datasets_by_company.keys():
        datasets_by_company[company] = dict()

# inputs values of question class into the nested dictionary based on company
for question_id in question_IDs:
    question_id_df = logic_df[logic_df['question_id'] == question_id]
    title = question_id_df['title'].unique()[0]
    company_name = question_id_df['company_name'].unique()[0]
    prompt = question_id_df['prompt'].unique()[0]
    question_type = question_id_df['question_type'].unique()[0]
    python_difficulty = question_id_df['python_difficulty'].unique()[0]
    sql_difficulty = question_id_df['mySQL_difficulty'].unique()[0]
    filesNames = list(question_id_df['file'].unique())

    f = title.split()
    f = map(str.capitalize, f)
    f = "".join(f)

    question = Question(question_id, title, prompt, question_type,
                        python_difficulty, sql_difficulty, filesNames, company_name)

    datasets_by_company[company_name][f] = question

# creates a dataframe of interview question from dictionary
data = dict()
for c in datasets_by_company.keys():
    for d in datasets_by_company[c].keys():
        sub_data = datasets_by_company[c][d]
        data[d] = vars(sub_data)
datas = pd.DataFrame(data).T

################################################################################################################################################################



# Title and sub-title for the web app.
st.write("""
# Interview Questions
""")

# selection box for company 
companies_ = list(logic_df["company_name"].unique())
companies_.insert(0, "All")
company_answer = st.selectbox("Select Company Name", companies_)

# selection box for difficulty of question based on company input
difficulties_ = list(logic_df[logic_df.company_name == company_answer]["python_difficulty"].unique())
difficulties_.insert(0, "All")
difficulty_answer = st.selectbox("Select Difficulty", map(str.capitalize,difficulties_))

#creates logic for main table
df = datas
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_selection(selection_mode="single", use_checkbox=True)
gridOptions = gb.build()

if(company_answer != "All"):
    df = df[df.company_name == company_answer]
    li = list(df.columns)
    li.remove("company_name")
    df = df[li]

if(difficulty_answer == "Hard"):
    df = df[df.python_difficulty == 'hard']
elif(difficulty_answer == "Medium"):
    df = df[df.python_difficulty == 'medium']
elif(difficulty_answer == "Easy"):
    df = df[df.python_difficulty == 'easy']

df.reset_index(inplace=True, drop=True)

# creates actual table
response = AgGrid(
    df,
    gridOptions=gridOptions,
    enable_enterprise_modules=True,
    update_mode=GridUpdateMode.MODEL_CHANGED,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
)

# info = response["selected_rows"]
# if(len(info) == 1):
#     df_ = pd.DataFrame(info)
#     st.write(df_)

usedDataSet = response["selected_rows"][0]["fileNames"]
usedDataSet = ast.literal_eval(usedDataSet)
st.write(usedDataSet)
# for f in usedDataSet:
#     continue
#     # df = getDatasetAsDataFrame(f)
#     # st.write(df.head())