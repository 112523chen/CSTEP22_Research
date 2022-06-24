import os
import pandas as pd

def getDatasetAsDataFrame(fileName):
    os.chdir("./datasets")
    # print(os.getcwd())
    df = pd.read_csv(fileName)
    os.chdir("../")
    # print(os.getcwd())
    return df

def getFinalResult(question):
    os.chdir("./Results")
    # print(os.getcwd())
    f = f"{question}.pkl"
    df = pd.read_pickle(f)
    os.chdir("../")
    # print(os.getcwd())
    return df

def getPythonSolution(question):
    os.chdir("./Solutions/Python")
    f = f"{question}.py"
    text_file = open(f,'r')
    python_solution = text_file.read()
    text_file.close()
    os.chdir("../..")
    return python_solution

def getSQLSolution(question):
    os.chdir("./Solutions/SQL")
    f = f"{question}.sql"
    text_file = open(f,"r")
    sql_solution = text_file.read()
    text_file.close()
    os.chdir("../..")
    return(sql_solution)

def getSolutions(question):
    python_solution = getPythonSolution(question)
    sql_solution = getSQLSolution(question)
    solution = f"Python Solution:\n{python_solution} \n\nSQL Solution:\n{sql_solution}"
    return solution