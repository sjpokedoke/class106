import csv
import plotly.express as px
import numpy as np

def getDataSource(datapath):
    sizeoftv = []
    averagetimespent = []

    with open(datapath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            sizeoftv.append(float(row["Size of TV"]))
            averagetimespent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return {"x": sizeoftv, "y": averagetimespent}

def findCorr(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between size of TV and average time spent watching TV: ")
    print(correlation[0,1])

def setup():
    datapath = "data3.csv"
    datasource = getDataSource(datapath)
    findCorr(datasource)

setup()