import pandas as pd
# -----------------------------------------------------------------------------
#1
# data = {
    # 'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone'],
    # 'Price': [1000, 800, 600, 1000, 800],
    # 'Store': ['BestBuy', 'Amazon', 'Walmart', 'BestBuy', 'Amazon']
# }

# df = pd.DataFrame(data)

# Проверка на дубликаты
# # print(df.info())
# print(df.duplicated())

# Удаление дубликатов
# df_cleaned = df.drop_duplicates()
# print(df_cleaned)
# -----------------------------------------------------------------------------

#2
# data = {
    # 'Item': ['TV', 'Fridge', 'Microwave', 'Washing Machine', 'Oven'],
    # 'Price': [400, 800, 50, 9000, 300]  # 9000 как выброс
# }

# df = pd.DataFrame(data)

# Q1 = df['Price'].quantile(0.25)
# Q3 = df['Price'].quantile(0.75)
# IQR = Q3 - Q1

# lower_bound = Q1 - 1.5 * IQR
# upper_bound = Q3 + 1.5 * IQR

# df_no_outliers = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]

# print(df_no_outliers)

# -----------------------------------------------------------------------------

#3
data = {
    'Employee': ['Alice', 'ALICE', 'Bob', 'BOB', 'Charlie'],
    'Department': ['Sales', 'sales', 'Marketing', 'marketing', 'IT']
}

df = pd.DataFrame(data)

df['Employee'] = df['Employee'].str.lower().str.capitalize()
df['Department'] = df['Department'].str.capitalize()

print(df)