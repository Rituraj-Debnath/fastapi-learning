from fastapi  import FastAPI 
import json


def p_data():
    with open("patient_data.json","r") as odin: #odin is just a var
        hella = json.load(odin)
        return hella  #hella is also a var


thor = FastAPI()   #thor is obj
@thor.get("/loki")

def asguard():
   stark = p_data() #start is also an var
   return stark

# all the var are storing values 
