import pandas as pd # data processing, CSV file I/O
import matplotlib.pyplot as plt # pyplot interface
import seaborn as sns # data visualization based on matplotlib
import numpy as np

from enum import Enum, auto


class PhysiologicParameters(Enum):
    TEMPF = 'Temperature'
    PULSE = 'Pulse Rate'
    RESPR = 'Respiration'
    BPSYS = 'Systolic Blood Pressure'
    BPDIAS ='Diastolic Blood Pressure'
    POPCT = 'Oxygen Saturation'
    SCORE = 'Score'


# Mean
def my_mean(sample):
    return sum(sample) / len(sample)


# Standard deviation of list
def standard_deviation(mean, sample):
    variance = sum([((x - mean) ** 2) for x in sample]) / len(sample)
    return (variance ** 0.5)


# Create histogram
def histogram(df):
    global PhysiologicParameters
    # iterating the columns
    for col in df.columns[1:]:
        mean = my_mean(df[col])
        print("mean : ", mean)
        print("standard deviation : ", standard_deviation(mean, df[col]))
        plt.title("Distribution of " + PhysiologicParameters[col].value,  fontsize = 16)
        plt.xlabel(col)
        df[col].plot(kind='hist')
        plt.savefig(col.lower() + ".pdf")
        plt.clf()


# Default heatmap
def heatmap(heartDiseases):
    p1 = sns.heatmap(heartDiseases.corr(), cmap='magma', annot=True)
    plt.show()


# Find outliers in dataset
def old_detect_outlier(data_1):
    threshold = 3
    mean_1 = np.mean(data_1)
    std_1 = np.std(data_1)

    for y in data_1:
        z_score = (y - mean_1) / std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers


# Find outliers in dataset
def detect_outlier(data):
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
df = pd.read_csv("data2.csv")

histogram(df)

heatmap(df)

old_detect_outlier(df)
