import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from random import randint

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
    CA = 'Number of major vessels'
    THAL = 'Thalium Stress Test result'
    TARGET = 'risk of heart disease'

def choice(firstOption):
    return "first" if firstOption == -1 else "second"


def oneCategoricalChoice(option, categoricalList):
    if option in categoricalList:
        return True
    return False


def menuOptions(colList, firstOption, categoricalList):
    print("Choose your", choice(firstOption), "Physiologic parameter :\n")
    i = 1
    while i < len(colList):
        if firstOption != i:
            if firstOption != -1 and (oneCategoricalChoice(firstOption, categoricalList) == True and oneCategoricalChoice(i, categoricalList) == True):
                print("[ X ] =>", PhysiologicParameters[colList[i]].value)
            else:
                print("[", i, "] =>", PhysiologicParameters[colList[i]].value)
        i = i + 1
    print("[ 0 ] => Exit")


def menu(colList, firstOption, categoricalList):
    option = -1
    while option < 0 or option > 14 and not option != 42:
        menuOptions(colList, firstOption, categoricalList)
        option = int(input("") or "42")
        if option == 42:
            print("You have chosen the default usage.")
            return option
        elif option < 0 or option > 14:
            print("Invalid option")
        elif option == firstOption:
            print("You already have selected", PhysiologicParameters[colList[option]].value, ". Please, choose an another parameter.")
            option = 0
        elif oneCategoricalChoice(firstOption, categoricalList) == True and oneCategoricalChoice(option, categoricalList) == True:
            print("You already have selected one categorical data. Please, choose an uncategorical.")
        elif option != 0:
            print(PhysiologicParameters[colList[option]].value, "has been choosed")
            if firstOption == -1:
                return menu(colList, option, categoricalList)
            else:
                return firstOption, option

def randomXAxis():
    return randint(1, 14)

def randomYAxis(x, categoricalList):
    y = x
    while y == x or (oneCategoricalChoice(y, categoricalList) == True and oneCategoricalChoice(x, categoricalList) == True):
        y = randint(1, 14)
    return y

data = pd.read_csv("data.csv")
categoricalList = [2, 3, 6, 7, 9, 11, 12, 13, 14]

res = menu(data.columns.values, -1, categoricalList)

if res == None:
    print("Exit")
    quit()

range = input("Choose range of point of the dataset between 0 and 303 : ")

if range and range.isdigit():
    if int(range) < 0 or int(range) > 303:
        range = '303'
    elif int(range) < 3:
        range = '3'
else:
    range = '303'

if (res != 42 and res[0] != 42 and res[1] != 42):
    x_value=data.columns.values[res[0]]
    y_value=data.columns.values[res[1]]

else:
    x = randomXAxis()
    x_value=data.columns.values[x]
    y_value=data.columns.values[randomYAxis(x, categoricalList)]
    
data = data.drop('ID', axis=1)
sns.jointplot(x=x_value, y=y_value, data=data.sample(int(range)), kind="kde", shade=True)
plt.show()