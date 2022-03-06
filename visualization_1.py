import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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


def oneCategoricalChoice(option):
    if option == 2 or option == 3 or option == 6 or option == 7 or option == 9 or option == 12 or option == 13 or option == 14:
        return True
    return False


def menuOptions(colList, firstOption):
    print("Choose your", choice(firstOption), "Physiologic parameter :\n")
    i = 1
    while i < len(colList):
        if firstOption != i:
            if firstOption != -1 and oneCategoricalChoice(i) == True:
                print("[ X ] =>", PhysiologicParameters[colList[i]].value)
            else:
                print("[", i, "] =>", PhysiologicParameters[colList[i]].value)
        i = i + 1
    print("[ 0 ] => Exit")


def menu(colList, firstOption):
    option = -1
    while option < 0 or option > 14 and not option != 42:
        menuOptions(colList, firstOption)
        option = int(input("") or "42")
        if option == 42:
            print("You have chosen the default usage.")
            return option
        elif option < 0 or option > 14:
            print("Invalid option")
        elif option == firstOption:
            print("You already have selected", PhysiologicParameters[colList[option]].value, ". Please, choose an another parameter.")
            option = 0
        elif oneCategoricalChoice(firstOption) == True and oneCategoricalChoice(option) == True:
            print("You already have selected one categorical data. Please, choose an uncategorical.")
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

range = input("Choose range of point of the dataset between 0 and 303 : ")

if range and range.isdigit():
    if int(range) < 0 or int(range) > 303:
        range = '303'
else:
    range = '303'

if res != 42 and res[0] != 42 and res[1] != 42:
    x_value=data.columns.values[res[0]]
    y_value=data.columns.values[res[1]]
    data = data.drop('ID', axis=1)
    if oneCategoricalChoice(res[0]) == False and oneCategoricalChoice(res[1]) == False:
        sns.scatterplot(x=x_value, y=y_value, data=data.sample(int(range)))
    else:
        sns.catplot(x=x_value, y=y_value, data=data.sample(int(range)))
else:
    data = data.drop(['ID', 'SEX', 'CP', 'FBS', 'RESTECG', 'EXANG', 'SLOPE', 'CA', 'THAL', 'TARGET'], axis=1)
    pd.plotting.scatter_matrix(data.sample(int(range)), figsize=(50,40))
plt.show()