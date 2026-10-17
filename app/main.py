from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from .schemas import PatientData, PredictionResponse
from .model import model


app = FastAPI(
    title="Breast Cancer Prediction API",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictionResponse)
def predict(patient: PatientData):
    data = pd.DataFrame([{
        "Age": patient.age,
        "T Stage": patient.t_stage,
        "N Stage": patient.n_stage,
        "6th Stage": patient.sixth_stage,
        "Grade": patient.grade,
        "A Stage": patient.a_stage,
        "Tumor Size": patient.tumor_size,
        "Estrogen Status": patient.estrogen_status,
        "Progesterone Status": patient.progesterone_status,
        "Reginol Node Positive": patient.regional_node_positive,
        "Survival Months": patient.survival_months,
    }])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0]

    status = "Alive" if prediction == 1 else "Dead"

    return {
        "prediction": int(prediction),
        "status": status,
        "probability": float(max(probability)),
    }

