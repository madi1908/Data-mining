import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#DataFrame
data = {
    'Age': [22, 35, 58, 45, 25],
    'Salary': [40000, 55000, 60000, 80000, 30000],
    'Purchased': [0, 1, 1, 0, 1]  # 0 = Not Purchased, 1 = Purchased
}

df = pd.DataFrame(data)

X = df.drop('Purchased', axis=1)  # 'Age' and 'Salary'
y = df['Purchased']  # Target: 'Purchased'

#70-30 and 80-20 splits
X_train_70, X_test_30, y_train_70, y_test_30 = train_test_split(X, y, test_size=0.3, random_state=42)
X_train_80, X_test_20, y_train_80, y_test_20 = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train_70, y_train_70)
predictions_70 = model.predict(X_test_30)
accuracy_70 = accuracy_score(y_test_30, predictions_70)

model.fit(X_train_80, y_train_80)
predictions_80 = model.predict(X_test_20)
accuracy_80 = accuracy_score(y_test_20, predictions_80)

print(f"Accuracy with 70-30 split: {accuracy_70:.2f}")
print(f"Accuracy with 80-20 split: {accuracy_80:.2f}")
