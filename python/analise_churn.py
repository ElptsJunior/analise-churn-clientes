import pandas as pd

df = pd.read_csv("dataset/churn.csv")

print(df.head())

print(df.info())

#Taxa de churn 
churn_rate = df["Churn"].value_counts(normalize=True)

print(churn_rate)

#Fatores de churn

#tipo de Contrato 
df.groupby("Contract")["Churn"].value_counts(normalize=True)
#Valor da Mensalidade
df.groupby("Churn")["MonthlyCharges"].mean()
