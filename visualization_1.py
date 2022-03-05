import pandas as pd
from matplotlib import pyplot as plt

from enum import Enum, auto

plt.style.use('seaborn')

class PhysiologicParameters(Enum):
    TEMPF = 'Temperature'
    PULSE = 'Pulse Rate'
    RESPR = 'Respiration'
    BPSYS = 'Systolic Blood Pressure'
    BPDIAS ='Diastolic Blood Pressure'
    POPCT = 'Oxygen Saturation'
    SCORE = 'Score'


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
    while option < 0 or option > 7:
        menuOptions(colList, firstOption)
        option = int(input(""))
        if option < 0 or option > 7:
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


data = pd.read_csv("data.csv")

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