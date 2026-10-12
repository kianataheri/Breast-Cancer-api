from pydantic import BaseModel


class PatientData(BaseModel):
    age: float
    t_stage: float
    n_stage: float
    sixth_stage: float
    grade: float
    a_stage: float
    tumor_size: float
    estrogen_status: float
    progesterone_status: float
    regional_node_positive: float
    survival_months: float


class PredictionResponse(BaseModel):
    prediction: int
    status: str
    probability: float

