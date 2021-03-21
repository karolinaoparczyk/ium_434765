import subprocess
import pandas as pd
from sklearn.model_selection import train_test_split

process = subprocess.Popen("kaggle datasets download -d alwinjoseph/stress-detection-of-medical-partitioners",
                           shell=True, stdout=subprocess.PIPE)
process.wait()
process = subprocess.Popen("tar -xf stress-detection-of-medical-partitioners.zip", shell=True, stdout=subprocess.PIPE)
process.wait()

data = pd.read_csv('data.csv')
data_train, data_test = train_test_split(data, test_size=50000, random_state=1, stratify=data["Alcohol_usage"])
print("All data")
print("Number of rows ", data.shape[0])
print("Number of columns ", data.shape[1])

print("\nTrain data")
print("Number of rows ", data_train.shape[0])
print("Number of columns ", data_train.shape[1])

print("\nTest data")
print("Number of rows ", data_test.shape[0])
print("Number of columns ", data_test.shape[1])

print("\n")
print(data.describe(include='all'))

print("\n")
print(data["Alcohol_usage"].value_counts())