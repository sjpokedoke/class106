import csv
import plotly.express as px
import numpy as np
import pandas as pd

def getDataSource(datapath):
    temperature = []
    icecreamsales = []

    with open(datapath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            temperature.append(float(row["Temperature"]))
            icecreamsales.append(float(row["Ice-cream Sales( ₹ )"]))
    return {"x": temperature, "y": icecreamsales}

def findCorr(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between temperature and ice cream sales: ")
    print(correlation[0,1])

def setup():
    datapath = "data.csv"
    datasource = getDataSource(datapath)
    findCorr(datasource)

setup()