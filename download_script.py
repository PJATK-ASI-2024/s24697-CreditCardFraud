import pandas as pd
from sklearn.model_selection import train_test_split

import kagglehub

# Wymaga uwierzytelnienia Kaggle https://www.kaggle.com/docs/api#authentication
path = kagglehub.dataset_download("dhanushnarayananr/credit-card-fraud", path='card_transdata.csv')

data = pd.read_csv(path) 
data = data.sample(n=5000, random_state=42)
train_data, retrain_data = train_test_split(data, test_size=0.3, random_state=42)

train_data.to_csv("data/train_data.csv", index=False)
retrain_data.to_csv("data/retrain_data.csv", index=False)
