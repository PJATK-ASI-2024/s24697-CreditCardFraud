from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd   

class FraudPredictionRequest(BaseModel):
    distance_from_home: float
    distance_from_last_transaction: float
    ratio_to_median_purchase_price: float
    repeat_retailer: int
    used_chip: int
    used_pin_number: int
    online_order: int

app = FastAPI()

model = joblib.load("./api/gradient_boosting_model.joblib")

@app.post("/predict")
def predict(request: FraudPredictionRequest):
    df = pd.DataFrame([request.dict()])
    prediction = model.predict(df)[0]
    return {"fraud": prediction}
