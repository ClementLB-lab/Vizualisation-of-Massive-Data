import pandas as pd # data processing, CSV file I/O
import matplotlib.pyplot as plt # pyplot interface
import seaborn as sns # data visualization based on matplotlib
import numpy as np

from enum import Enum, auto


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
    OLDPEAK = 'ST wave induced by exercise relative to rest'
    SLOPE = 'Slope of the peak exercise ST segment'
    CA = 'Number of major vessels'
    THAL = 'Thalium Stress Test result'
    TARGET = 'risk of heart disease'


# Mean
def my_mean(sample):
    return sum(sample) / len(sample)


# Standard deviation of list
def standard_deviation(mean, sample):
    variance = sum([((x - mean) ** 2) for x in sample]) / len(sample)
    return (variance ** 0.5)


# Find outliers in dataset with Using Z score
def detect_outlier(data_):
    outliers = []
    threshold = 3
    nb_outliers = 0
    mean_ = my_mean(data_)
    std_ = standard_deviation(mean_, data_)
    
    for y in data_:
        z_score= (y - mean_) / std_ 
        if np.abs(z_score) > threshold:
            outliers.append(y)
            nb_outliers += 1
    
    if nb_outliers != 0:
        print("Number of outliers found: ", nb_outliers, "\nHere is the list of outliers :", end = '')
        for outlier in outliers:
            print(" ", outlier, end = '')

    else:
        print("There is no outliers", end = '')


# Create histogram
def histogram(df):
    global PhysiologicParameters
    # iterating the columns
    for col in df.columns[1:]:
        mean = round(my_mean(df[col]), 2)
        std = round(standard_deviation(mean, df[col]), 2)
        print("\n\n-----", PhysiologicParameters[col].value, "-----\nMean : ", mean, "\nStandard Deviation : ", std)
        detect_outlier(df[col])
        plt.title("Distribution of " + PhysiologicParameters[col].value + ':\n' + f'$\mu={mean}$, $\sigma={std}$',  fontsize = 16)
        plt.xlabel(col)
        df[col].plot(kind='hist')
        plt.savefig(col.lower() + ".pdf")
        print("\n\n" + col.lower() + ".pdf generated")
        plt.clf()


# Default heatmap
def heatmap(heartDiseases):
    p1 = sns.heatmap(heartDiseases.corr(), cmap='magma', annot=True)
    plt.show()


# Find outliers in dataset
def old_detect_outlier(data):
    nb_points = data.shape[0]

    print("nb_points", nb_points)

    # compute center
    center = np.mean(data, axis=0)
    print("compute center", center)

    metric = "custom"

    # Toutes les première colonnes
    std_x = np.std(data[:, 0])
    # Toutes les secondes colonnes
    std_y = np.std(data[:, 1])
    # factor = 5
    differences = data-center
    differences[:, 0] /= std_x
    differences[:, 1] /= std_y
    abs_differences = np.abs(differences)
    distances = np.sum(abs_differences, axis=1)
    sum_distances = np.sum(distances)
    mean_distance_to_center = sum_distances/nb_points

    nb_outliers = 0
    for index in range(nb_points):
        datapoint = data[index]
        vector_to_center = datapoint-center
        distance_to_center = abs(vector_to_center[0]/std_x)+abs(vector_to_center[1]/std_y)
        if distance_to_center > 2.5*mean_distance_to_center:
            print(datapoint)
            print(distance_to_center/mean_distance_to_center)
            print("")
            plt.plot(datapoint[0], datapoint[1], "o", color="red", markersize=1.5)
            nb_outliers += 1
    print(f"{nb_outliers} outliers")

    plt.title(f"outliers in red, {metric} metric")
    plt.savefig(f"outliers, metric={metric}.pdf")
    plt.close()


# making data frame 
df = pd.read_csv("heart.csv")

histogram(df)

heatmap(df)