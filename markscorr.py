import csv
import plotly.express as px
import numpy as np

def getDataSource(datapath):
    dayspresent = []
    marks = []

    with open(datapath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            dayspresent.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
    return {"x": dayspresent, "y": marks}

def findCorr(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between days present and marks in percentage of a student: ")
    print(correlation[0,1])

def setup():
    datapath = "data4.csv"
    datasource = getDataSource(datapath)
    findCorr(datasource)

setup()