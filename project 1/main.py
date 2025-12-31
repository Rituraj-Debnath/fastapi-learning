from fastapi import FastAPI  
import json
from fastapi import Path
# Path is a helper function used to provide metadata, description, data validation for our path parameters so user can understand before giving input

def p_data():
    with open("patient_data.json","r") as odin: #odin is just a var
        hella = json.load(odin)
        return hella  #hella is also a var


app = FastAPI()   #app is obj
@app.get("/loki")

def asguard():
   stark = p_data() #start is also an var
   return stark

# all the var are storing values 


#### adding the concept of query/path parameters

@app.get("/only/{patient_id}")
def only(patient_id: str = Path(..., description="write patient id here", example="001,002" , min_length=3)):
    data = p_data()
    if patient_id in data:
        return data[patient_id]
    return {"error": "patient not found"}