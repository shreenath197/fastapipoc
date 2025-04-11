from fastapi import FastAPI
from claim_model_prediction import Claim
import pandas as pd
import joblib

app= FastAPI(
    title="Insurance Claim Prediction Amount Model",
    description="API providong Insurance Claim Prediction Amount based on input features"
)
@app.get("/")
def index():
    return "Great !!Wecome to the Claim Amount Prediction Model"

@app.post("/predict")
def make_Prediction(claim: Claim):
    new = pd.DataFrame(data=dict(
        wind=[claim.wind],
        rain=[claim.rain],
        area=[claim.area]
    ))

    model = joblib.load("svm_Linear.joblib")
    prediction = model.predict(new)
    return {"prediction": prediction[0]}
print("done")

    


