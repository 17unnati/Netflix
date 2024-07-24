# (graph not printed,A heatmap is a two-dimensional graphical representation of data
import seaborn as sns
import pandas as pd
data = pd.read_csv(
    r"C:\Users\Unnati Chaurasiya\Downloads\Netflix Database.csv")
print(data)
print(data.head())
print(data.columns)
           # for printing a particular coloumn
print(data[['Release_Date']].to_string(index=False))
print(data.tail())
print(data.size)
print(data.shape)
print(data.columns)
print(data.dtypes)
print(data.info())
print(data[data.duplicated()])
print(data.drop_duplicates(inplace=True))
print(data.isnull())
print(data.isnull().sum())


# where the individual values that are contained in a matrix are represented as colours)
print(sns.heatmp(data.isnull()))

# 1) For House Of Cards what is the show id and  who is the director of this show?
# by isin()
print(data[data['Title'].isin(['House of Cards'])])
# # by str.contains()
# print(data[data['Title'].str.contains('House of Cards')])

# 2) IN which year highest no. of TV shows and movies were released? Show with bargraph.
# by to_datetime

# data['Date_N']=pd.to_datetime(data['Release_Date'])
# print(data.head())
# print(data['Release_Date'].dt.year.value_counts().plot(kind='bar'))

# 3)How many movie and TV shows are in the dataset? Show with the bargraph

print(data.groupby('Category').Category.count())

# bargraph : by countplot()
print(sns.countplot(data['Category']))
