from fastapi import FastAPI , HTTPException
import json
from pydantic import BaseModel , Field
from fastapi.responses import JSONResponse

from typing import Annotated #this tells python that we are adding extra rules for data validation so dont mark it as yellow lines.

### a req body is a json data that we send in a POST req with the fields to add new data.
#### json data loading here ###
def load_data():
    with open("patient_data.json") as file:
        data=json.load(file)
    return data

### /home for getting all data.
app = FastAPI()
@app.get("/home")
def get_whole_data():
    return load_data()


class Patient(BaseModel):  #creating a class named patient inherinting base model
    id: Annotated[str, Field(..., description="ID of the patient")]
    name: Annotated[str, Field(..., description="Name of the patient", examples=["Rituraj"])]
    age: Annotated[int, Field(..., gt=0, lt=120, examples=[42])]
    disease: Annotated[str, Field(..., description="Disease name")]
    stage: Annotated[str, Field(..., description="Disease stage", examples=["critical"])]
    bmi: Annotated[float, Field(..., gt=0, lt=70, examples=[33.5])]

    #### why we are adding all these metadata like description things ?
    # so that anyone who will be using our api will get a complete overview in the docs page.

@app.post("/create")

def create_patient(validated_data : Patient):
    ## here the data in json is going to Pydantic base model , after data validation the data will be saved inside the validated_data variable, so the flow is like json_data of request body -> pydantic base model -> Validation -> validated_data

    # loading existing data
    data = load_data()

    #checking if the validated_data exist on the existing data or not using patient id
    if validated_data.id in data:
        raise HTTPException(status_code=403 , detail="Patient already exists")
    
    #adding new patient data
    data[validated_data.id] = validated_data.model_dump(exclude=["id"])
    

    # a func to add new data to existing json file
    def save_data(data):
        with open("patient_data.json", "w") as f:
            json.dump(data,f,indent=4) #indent =4 , means without this the json data will be dumpted as a single line without indentation.

    #saving into json file.

    save_data(data)

    #Returning a response 
    return JSONResponse(status_code=201, content={'message': 'patient created successfully'})

    



