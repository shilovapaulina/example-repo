import pandas as pd
df = pd.read_csv('us-news-univ-rankings-2017.csv')

for column in ['Tuition and fees','In-state']:
    df[column] = df[column].replace('$','')
    df[column] = df[column].replace(',','')
    df[column] = df[column].astype(float)

print(df.head())