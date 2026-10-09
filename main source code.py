# Loan Approval/Rejection model
import pandas as pd
# read data set
print("-------------------")
print("---Data Analysis---")
print("-------------------")
data=pd.read_csv("loan_data_1.csv")
# Data set
print(data)
print("-------------------------")
print("---Using Head Function---")
print("-------------------------")
# Using head function to print 1st 5 rows from dataset
print(data.head())
print("-------------------------")
print("---Using Tail Function---")
print("-------------------------")
# Using tail function
print(data.tail())
print("-------------------------")
print("---Using Info Function---")
print("-------------------------")
# Using info function to print information about data
print(data.info())
print("-----------------------------")
print("---Using Describe Function---")
print("-----------------------------")
# Using describe function
print(data.describe())
# Data preprossesing 
# checking null values
print("------------------------")
print("---Data Preprocessing---")
print("------------------------")
print("---Removing Irrelevant Data---")
print("------------------------------")

# Removing Irrelevant data 
data=data.drop(["Unnamed: 0","Loan_ID"],axis=1)
print(data)
# Handling Missing Values
print("-----------------------------")
print("---Handling Missing Values---")
print("-----------------------------")

# print(data["Dependents"].mode())
print(data.isnull().sum())
data['Dependents']=data['Dependents'].fillna(data['Dependents'].mode()[0])

data["Self_Employed"]=data["Self_Employed"].fillna(data["Self_Employed"].mode()[0])

data["ApplicantIncome"]=data["ApplicantIncome"].fillna(data["ApplicantIncome"].mean())

data["CoapplicantIncome"]=data["CoapplicantIncome"].fillna(data["CoapplicantIncome"].median())

data["LoanAmount"]=data["LoanAmount"].fillna(data["LoanAmount"].median())

data["Loan_Amount_Term"]=data["Loan_Amount_Term"].fillna(data['Loan_Amount_Term'].mode()[0])

data["Credit_History"]=data["Credit_History"].fillna(data["Credit_History"].mode()[0])
print("-----------------------------")
print("---Checking Missing Values---")
print("-----------------------------")
# Checking If all the null values are handled or not
print(data.isnull().sum())
print("-------------------------------")
print("---Checking Duplicate Values---")
print("-------------------------------")
# Checking Duplicate values
print(data.duplicated().sum())
data=data.drop_duplicates()
print()
print(data.duplicated().sum())
# Handling Text daata
print("---------------------------")
print("---Handling Textual Data---")
print("---------------------------")
from sklearn.preprocessing import LabelEncoder
Le=LabelEncoder()
print("---Transforming Gender Column---")
print(data["Gender"].value_counts())
data["Gender"]=Le.fit_transform(data["Gender"])
print(data["Gender"].value_counts())

print("---Transforming Education Column---")
print(data["Education"].value_counts())
data["Education"]=Le.fit_transform(data["Education"])
print(data["Education"].value_counts())

print("---Transforming Married Column---")
print(data["Married"].value_counts())
data["Married"]=Le.fit_transform(data["Married"])
print(data["Married"].value_counts())

print("---Transforming Self_Employed Column---")
print(data["Self_Employed"].value_counts())
data["Self_Employed"]=Le.fit_transform(data["Self_Employed"])
print(data["Self_Employed"].value_counts())

print("---Transforming Property_Area Column---")
print(data["Property_Area"].value_counts())
data["Property_Area"]=Le.fit_transform(data["Property_Area"])
print(data["Property_Area"].value_counts())

print("---Transforming Loan_Status Column---")
print(data["Loan_Status"].value_counts())
data["Loan_Status"]=Le.fit_transform(data["Loan_Status"])
print(data["Loan_Status"].value_counts())

print("---Transforming Dependents Column---")
print(data["Dependents"].value_counts())
data["Dependents"]=Le.fit_transform(data["Dependents"])
print(data["Dependents"].value_counts())

print("---------------------------")
print("---Printing Cleaned Data---")
print("---------------------------")
print(data)

# Data Visualization using Seaborn library

print("------------------------")
print("---Data Visualization---")
print("------------------------")

import matplotlib.pyplot as plt
import seaborn as sns

print("---HeatMap---")
print("-------------")

sns.heatmap(data.corr())
plt.show()

print("---PairPlot Graph ---")
print("---------------------")

sns.pairplot(data)
plt.show()

print("---------------------------------------------")
print("Spliting Data Into Features & Target Vriables")
print("---------------------------------------------")

x=data.drop("Loan_Status",axis=1)
y=data["Loan_Status"]

print(x)
print(y)

from sklearn.model_selection import train_test_split
# Spliting x(input),y(output) into training and testing data in ratio 80:20 80(training data),20(testing data) training data>testing data
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.7,test_size=0.3,shuffle=True,random_state=42)

print("---------------------")

print(x_train.shape)

print(x_test.shape)

print(y_train.shape)

print(y_test.shape)

# Model Training Using Sk-learn 
# For Classification - Logistic Regression 
# For Regression - Linear Regression
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
print("-------------------------------")
print("--PREDICTION ON TRAINING DATA--")
x_training_predict=model.predict(x_train)
print(x_training_predict)

print("------------------------------")
print("--PREDICTION ON TESTING DATA--")
x_testing_predict=model.predict(x_test)
print(x_testing_predict)

from sklearn.metrics import accuracy_score,classification_report, confusion_matrix,precision_score,recall_score,f1_score

print("----------------------")
print("---MODEL EVALUATION---")

print("--------------------------")
print("--TRAINING DATA ACCURACY--")
accuracy_train=accuracy_score(y_train,x_training_predict)
print(accuracy_train*100,"%")


print("--------------------------")
print("--TESTING DATA ACCURACY--")
accuracy_test=accuracy_score(y_test,x_testing_predict)
print(accuracy_test*100,"%")

precision = precision_score(y_test,x_testing_predict, zero_division=0)
recall = recall_score(y_test,x_testing_predict, zero_division=0)
f1 = f1_score(y_test, x_testing_predict, zero_division=0)

print("----------------------------")
print(f"Precision : {precision:.2%}")

print("-------------------------")
print(f"Recall    : {recall:.2%}")

print("---------------------")
print(f"F1-Score  : {f1:.2%}")


# Generate confusion matrix
cm = confusion_matrix(y_test,x_testing_predict)

print("-------------------")
print("\nConfusion Matrix:")
print(cm)




