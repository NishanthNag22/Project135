import pandas as pd
import plotly_express as px
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("filter_stars.csv")

df.drop(['Unnamed: 0', 'Unnamed: 0.1'],axis=1,inplace=True)

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

sns.barplot(x = name,y = mass)
plt.title("STAR NAMES VS MASS")
plt.xlabel('NAMES')
plt.ylabel('MASS')
plt.show()
plt.figure()

sns.barplot(x = name,y = radius)
plt.title("STAR NAMES VS RADIUS")
plt.xlabel('NAMES')
plt.ylabel('RADIUS')
plt.show()
plt.figure()

sns.barplot(x = name,y = dist)
plt.title("STAR NAMES VS DISTANCE")
plt.xlabel('NAMES')
plt.ylabel('DISTANCE')
plt.show()
plt.figure()

sns.barplot(x = name,y = gravity)
plt.title("STAR NAMES VS GRAVITY")
plt.xlabel('NAMES')
plt.ylabel('GRAVITY')
plt.show()