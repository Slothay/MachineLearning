import pandas as pd

folder = "C:\\Users\\peter\\OneDrive - Mölk Utbildning\\2023 - Q4\\Kursmaterial\\M10 - Machine Learning (6 days)\\Day 4 - SVM\\"
filename = "SMHI_pthbv_p_t_1961_2022_yearly_4326.csv"

df = pd.read_csv(folder+filename,sep=';')

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df['tidpunkt'].to_frame(),df['temperatur'].to_frame())

print(model.predict([[2030]]))
