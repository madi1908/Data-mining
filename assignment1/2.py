import pandas as pd
df = pd.read_csv('Apple_price_to_clean.csv')

# print(df.isnull().sum()) #determining the amount of missing data
# df_cleaned = df.dropna() #Removing rows with missing values

# fillna() method allows you to fill in missing values
# df['Open'].fillna(df['Open'].mean(), inplace=True)  #mean value
# df['Open'].fillna(df['Open'].median(), inplace=True) #median value

data = {'Open': ['27.777500', None, '26.772499', '', '28.042500', '27.537500']}
df = pd.DataFrame(data)
# df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
# df['Open'] = df['Open'].fillna(df['Open'].mean())
print(df)

# df['Open'].ffill(inplace=True) #replace previous value
df['Open'].bfill(inplace=True) #replace next value
print(df)