import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv

df=pd.read_csv("titanic.csv")
#Exploratory Data Analysis
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info)
print(df.isnull().sum())


#Data Cleaning
#Dropping dulicate coulumns
print(df.shape)
df=df.drop_duplicates()
print(df.shape)


#handling Missing Numeric data
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Fare"]=df["Fare"].fillna(df["Fare"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

df=df.dropna(subset=["Name","Ticket"])

#Typecasting
df["Age"]=df["Age"].astype(int)
df["Sex"]=df["Sex"].str.strip().str.lower()


#Data Preprocessing
df=df.rename(columns={"Survived" :"is_survived"})

df["Sex"]=df["Sex"].map({"male":1,"female":0})
df=df.rename(columns={"Sex" :"is_male"})
#Dropping the cabin Columns
df=df.drop(columns=["Cabin"])
print(df.shape)
print(df.head())
print(df.tail())
print(df.describe())
print(df.info)
print(df.isnull().sum())
print(df.head(30))