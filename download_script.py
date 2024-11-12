import pandas as pd
from sklearn.model_selection import train_test_split

import kagglehub

path = kagglehub.dataset_download("dhanushnarayananr/credit-card-fraud", force_download=True)
data = pd.read_csv( f'{path}/card_transdata.csv') 
data = data.sample(n=50000, random_state=42)
train_data, retrain_data = train_test_split(data, test_size=0.3, random_state=42)

train_data.to_csv("data/train_data.csv", index=False)
retrain_data.to_csv("data/retrain_data.csv", index=False)
data.to_csv("data/data.csv", index=False)

