#1
# from sklearn.preprocessing import MinMaxScaler
# import pandas as pd

# data = pd.DataFrame({
#     'score': [100, 150, 200, 250, 300]
# })

# scaler = MinMaxScaler()
# data[['score']] = scaler.fit_transform(data[['score']])
# print(data)

# -----------------------------------------------------------------------------

#2
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder

# data = pd.DataFrame({
#     'Type': ['X', 'Y', 'Z', 'X'],
#     'Amount': [5, 10, 5, 15]
# })

# encoder = OneHotEncoder(sparse_output=False)
# encoded = encoder.fit_transform(data[['Type']])

# encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['Type']))

# final_data = pd.concat([data.drop('Type', axis=1), encoded_df], axis=1)
# print(final_data)

# -----------------------------------------------------------------------------
#3

import pandas as pd

data = pd.DataFrame({
    'Score': [8, 18, 28, 38, 48, 58, 68, 78, 88, 98]
})

intervals = [0, 25, 50, 75, 100]
categories = ['Low', 'Medium', 'High', 'Very High']

data['Score_Group'] = pd.cut(data['Score'], bins=intervals, labels=categories)
print(data)
