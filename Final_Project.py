
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd


df = pd.read_csv('heart.csv', delimiter=',')
sns.countplot(x="target", data=df, palette="bwr")
plt.title("Number of Patients Have and Don't Heart Disease(0 = Don't-1 = Have)")
plt.show()


countNoDisease = len(df[df.target == 0])
countHaveDisease = len(df[df.target == 1])
print("Percentage of Patients that DO NOT Have Heart Disease: {:.2f}%".format((countNoDisease / (len(df.target))*100)))
print("Percentage of Patients Have Heart Disease: {:.2f}%".format((countHaveDisease / (len(df.target))*100)))



sns.countplot(x='sex', data=df, palette="mako_r")
plt.title("Number of Female and Male Patients")
plt.xlabel("Sex (0 = female, 1= male)")
plt.legend(["0 = Female 1 = Male"])
plt.show()



countFemale = len(df[df.sex == 0])
countMale = len(df[df.sex == 1])
print("Percentage of Female Patients: {:.2f}%".format((countFemale / (len(df.sex))*100)))
print("Percentage of Male Patients: {:.2f}%".format((countMale / (len(df.sex))*100)))


pd.crosstab(df.age,df.target).plot(kind="bar",figsize=(20,6))
plt.title('Heart Disease Frequency for Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend(["Don't have disease" , "Have Disease"])
plt.show()


pd.crosstab(df.sex,df.target).plot(kind="bar",figsize=(15,6),color=['yellow','black' ])
plt.title('Heart Disease Frequency for Sex')
plt.xlabel('Sex (0 = Female, 1 = Male)')
plt.xticks(rotation=0)
plt.legend(["Haven't Disease", "Have Disease"])
plt.ylabel('Frequency')
plt.show()



plt.scatter(x=df.age[df.target==1], y=df.thalach[(df.target==1)], c="red")
plt.scatter(x=df.age[df.target==0], y=df.thalach[(df.target==0)])
plt.legend(["Disease", "Not Disease"])
plt.xlabel("Age")
plt.ylabel("Maximum Heart Rate")
plt.title('Heart Disease Based on Heart Rate')
plt.show()



pd.crosstab(df.fbs,df.target).plot(kind="bar",figsize=(15,6),color=['blue','orange' ])
plt.title('Heart Disease Frequency According To FBS')
plt.xlabel('FBS - (Fasting Blood Sugar > 120 mg/dl) (1 = true; 0 = false)')
plt.xticks(rotation = 0)
plt.legend(["Haven't Disease", "Have Disease"])
plt.ylabel('Frequency of Disease or Not')
plt.show()

pd.crosstab(df.cp,df.target).plot(kind="bar",figsize=(15,6),color=['red','yellow' ])
plt.title('Heart Disease Frequency According To Chest Pain Type')
plt.xlabel('Chest Pain Type')
plt.xticks(rotation = 0)
plt.legend(["Don't have", "Have"])
plt.ylabel('Frequency of Disease or Not')
plt.show()

pd.crosstab(df.trestbps,df.target).plot(kind="bar",figsize=(20,6),color=['orange','black' ])
plt.title('Heart Disease Frequency According To Blood Pressure Type')
plt.xlabel('blood pressure')
plt.legend(["Don't have", "Have"])
plt.ylabel('Frequency of Disease or Not')
plt.show()

 
