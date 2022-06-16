import os
import pandas as pd

def getDatasetAsDataFrame(fileName):
    os.chdir("./datasets")
    print(os.getcwd())
    df = pd.read_csv(fileName)
    os.chdir("../")
    return df