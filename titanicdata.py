# method to import file in python
# import pandas as pd
# data= pd.read_csv("Titanic.csv")
# print(data.head())                #it will show the first 5 rows
# print(data.shape)                 #it will shows how manys rows and columns are there(899, 12)
# print(data.info())                #it will shows all 12 columns+ data types + missing values
# print(data.columns)               #it will shows only columns name


import pandas as pd
data = pd.read_csv("Titanic.csv")
# pd.set_option('display.max_columns', None)
# print(data.head())
# print(data.isnull().sum())                 # to find the missing values in every columns if isnull is been used then it shows the true or false 
                                            #inthat true means missing so for better understand we need to add isnull().sum()
data['Age']= data['Age'].fillna(data['Age'].mean())   # to fill data of age as age is numerical value so we usually fill it by mean(average)
data['Embarked']= data['Embarked'].fillna(data['Embarked'].mode()[0])  # embarked is categorical column (C, Q, S) so we fill it by mode (most frequent value)
data= data.drop('Cabin', axis=1)                                  # to drop the column besause it has more than 75% of data missing in it

# print(data.head())
# print(data.isnull().sum())
# print(data.info())


# now converting the catergorical features like name, sex, embarked etc into numerical value so that computer can understand
data['Sex']= data['Sex'].map({'male':0, 'female':1})
# print(data.head())

# now embarked that means where the passenger boarded
data['Embarked']= data['Embarked'].map({'S':0, 'C':1, 'Q':2})
# print(data.head())


#now dropping the unnessarry columns that are name, ticket and passenger id..
data= data.drop(['PassengerId', 'Name', 'Ticket'], axis=1)
# print(data.head())


# firstly we need to import visualization libraries:
import matplotlib.pyplot as plt
import seaborn as sns

# to see survival count in bar chart
# plt.figure(figsize=(6,4))
# sns.countplot(x='Survived', data=data)
# plt.title("Survival Count")
# plt.xlabel("0 = Died, 1 = Survived")
# plt.ylabel("Number Of Passengers")
# plt.show()


#To see Survival by gender :
# plt.figure(figsize=(6,4))
# sns.countplot(x="Sex", data=data)
# plt.title("Survival by Gender")
# plt.xlabel("0 = Male, 1 = Female")
# plt.ylabel("Number of Passengers")
# plt.show()


#Pclass vs Survival
# plt.figure(figsize=(6,4))
# sns.countplot(x="Pclass", hue="Survived", data=data)
# plt.title("Pclass vs Survived")
# plt.xlabel("Class(1= 1st, 2= 2nd, 3= 3rd)")
# plt.ylabel("Number of Passengers")
# plt.show()


# Age Distribution
# plt.figure(figsize=(6,4))
# sns.histplot(data['Age'], bins=30, kde=True)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Number of Passengers")
# plt.show()