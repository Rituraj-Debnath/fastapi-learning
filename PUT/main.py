from fastapi import FastAPI , HTTPException
import json
from pydantic import BaseModel , Field
from fastapi.responses import JSONResponse

from typing import Annotated , Optional #this tells python that we are adding extra rules for data validation so dont mark it as yellow lines.

app = FastAPI()

def load_data():
    with open("patient_data.json") as file:
        data=json.load(file)
    return data

def save_data(data):
        with open("patient_data.json", "w") as f:
            json.dump(data,f,indent=4) #indent =4 , means without this the json data will be dumpted as a single line without indentation.


class Patient_update(BaseModel):
    name: Annotated [Optional[str], Field(description="Name of the patient", default=None ) ]
    age: Annotated [Optional[int], Field(gt=0, lt=120, default=None)]
    disease: Annotated [Optional[str], Field(default=None, description="Disease name")]
    stage: Annotated[Optional[str], Field( default=None, description="Disease stage")]
    bmi: Annotated [Optional[float], Field(default=None, gt=0, lt=70 )]


@app.put("/update/{p_id}")
def update_patient(p_id: str, updated_data: Patient_update):
    loaded = load_data()
    if p_id not in loaded:
        raise HTTPException(status_code=404, detail="Patient not found for update")

    existing_patient_data = loaded[p_id]

    updated_patient_data = updated_data.model_dump(exclude_unset=True) 

    for key,value in updated_patient_data.items:
        existing_patient_data[key] = value

        loaded[p_id] = existing_patient_data 

        save_data(loaded)