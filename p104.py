import csv
import pandas as pnd
import plotly.express as px
from collections import Counter


with open('HeightWeight.csv', newline = '') as file :
    reader = csv.reader(file)
    fileData = list(reader)
fileData.pop(0)

newData = []
for i in range(len(fileData)):
    nextNum = fileData[i][2]
    newData.append(float(nextNum))

dataLength = len(newData)
total = 0
for i in newData:
    total += i
mean = total/dataLength
print("Mean Value = " + str(mean))

newData.sort()
if dataLength%2 == 0:
    median1 = float(newData[dataLength//2])
    median2 = float(newData[(dataLength//2)-1])
    median = (median1 + median2)/2
else:
    median = newData[dataLength//
                     2]
print("Here is your Median : " + str(median))

data = Counter(newData)
modeRange = {"100-120": 0, "120-140":0, "140-160":0}
for Weight,Occurance in data.items():
    if 100 < float(Weight) < 120:
        modeRange["100-120"] += Occurance
    elif 120 < float(Weight) < 140:
        modeRange["120-140"] += Occurance
    elif 140 < float(Weight) < 160:
        modeRange["140-160"] += Occurance

mode_Range , mode_Occurance = 0,0
for range, Occurance in modeRange.items():
    if(Occurance > mode_Occurance):
        mode_Range, mode_Occurance = [int(range.split("-")[0]), int(range.split("-")[1])], Occurance
mode = float((mode_Range[0] + mode_Range[1]) / 2)
             
print(f"Mode is ->  + {mode:2f}")
             
