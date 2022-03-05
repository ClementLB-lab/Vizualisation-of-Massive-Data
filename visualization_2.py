import pandas as pd
from matplotlib import pyplot as plt

from enum import Enum, auto

plt.style.use('seaborn')

class PhysiologicParameters(Enum):
    AGE = "Age"
    SEX = "Sex"
    CP = "Chest Pain Type"
    TRESTBPS = "Resting Blood Pressure"
    CHOL = "Serum Cholestoral"
    FBS = "Fasting Blood Sugar"
    RESTECG = "Resting Electrocardiographic Results"
    THALACH = 'Maximum Heart Rate Achieved'
    EXANG = 'Exercise Induced Angina'
    OLDPEAK = 'ST depression induced by exercise relative to rest'
    SLOPE = 'Slope of the peak exercise ST segment'

def choice(firstOption):
    return "first" if firstOption == -1 else "second"


def menuOptions(colList, firstOption):
    print("Choose your", choice(firstOption), "Physiologic parameter :\n")
    i = 1
    while i < len(colList):
        if firstOption != i:
            print("[", i, "] =>", PhysiologicParameters[colList[i]].value)
        i = i + 1
    print("[ 0 ] => Exit")


def menu(colList, firstOption):
    option = -1
    while option < 0 or option > 11:
        menuOptions(colList, firstOption)
        option = int(input(""))
        if option < 0 or option > 11:
            print("Invalid option")
        elif option == firstOption:
            print("You already have selected", PhysiologicParameters[colList[option]].value, ". Please, choose an another parameter.")
            option = 0
        elif option != 0:
            print(PhysiologicParameters[colList[option]].value, "has been choosed")
            if firstOption == -1:
                return menu(colList, option)
            else:
                return firstOption, option


data = pd.read_csv("heart.csv")

res = menu(data.columns.values, -1)

if res == None:
    print("Exit")
    quit()

x = data[data.columns[res[0]]].values
print(x)
y = data[data.columns[res[1]]].values
print(y)

plt.scatter(x, y)

plt.tight_layout()
plt.show()