from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

# import the ml model
with open('model_1.pkl', 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

# pydantic model to validate incoming data
class UserInput(BaseModel):

    Applicant_Income: Annotated[float, Field(..., gt=0, description='Income of the user')]
    Coapplicant_Income: Annotated[float, Field(..., gt=0, description='Income of the co applicant user')]
    Employment_Status: Annotated[Literal['Salaried', 'Self-employed', 'Contract', 'Unemployed'], Field(..., description='Employment status')]
    Marital_Status: Annotated[Literal['Married', 'Single'], Field(...,  description='Married or single')]
    Age: Annotated[float, Field(..., gt=0, description='Age')]
    Dependents: Annotated[int, Field(..., description='Number of dependent')]
    Credit_Score: Annotated[float, Field(..., description='Credit Score')]
    Existing_Loans: Annotated[int, Field(..., description='No of Exisiting loan')]
    DTI_Ratio: Annotated[float, Field(..., gt=0, lt=1, description='Income of the user')]
    Savings: Annotated[int, Field(..., gt=0, description='Savings')]
    Collateral_Value: Annotated[int, Field(..., gt=0, description='Collateral Value')]
    Loan_Amount: Annotated[float, Field(..., gt=0, description='Loan Amount')]
    Loan_Term: Annotated[float, Field(..., gt=0, description='Loan duration in months')]
    Loan_Purpose: Annotated[Literal['Personal', 'Car', 'Business', 'Home', 'Education'], Field(..., description='Purpose of Loan')]
    Property_Area: Annotated[Literal['Urban', 'Semiurban', 'Rural'], Field(..., description='Property type')]
    Education_Level: Annotated[Literal['Not Graduate', 'Graduate'], Field(..., description='Graduate or not')]
    Gender: Annotated[Literal['Male', 'Female'], Field(..., description= 'Gender of the user')]
    Employer_Category: Annotated[Literal['Private', 'Government', 'Unemployed', 'MNC', 'Business'], Field(..., description='employer category')]
    
@app.post('/predict')
def predict_premium(data: UserInput):

    input_dict = data.model_dump()
    input_df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_df)

    return {"predicted_category": prediction.tolist()}
