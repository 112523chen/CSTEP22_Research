import os
import pandas as pd

def getDatasetAsDataFrame(fileName):
    os.chdir("../datasets")
    df = pd.read_csv(fileName)
    os.chdir("../")