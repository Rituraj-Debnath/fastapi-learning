from fastapi import FastAPI , Path , HTTPException , Query
import json

# Path is a helper function used to provide metadata, description, data validation for our path parameters so user can understand before giving input
#Httpexception is a build it exception class in fastapi to provide custom http error response in our api.


def p_data():  #loading the json data here
    with open("patient_data.json","r") as odin: #odin is just a var
        hella = json.load(odin)
        return hella  #hella is also a var


app = FastAPI()   #app is obj
@app.get("/loki")
def asguard():
   stark = p_data() #stark is also an var
   return stark

# all the var are storing values 


#### adding the concept of path parameters

@app.get("/only/{patient_id}")  ##patient_id is the path param
def only(patient_id: str = Path(..., description="write patient id here", example="004" , min_length=3)): #here {patient_id} & patient_id parameter names should match.(it can be any name but should match both names)
    data = p_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404 , detail="The patient is not present in our database")


#lets use query params ,that are optional key value pairs used for searching,sorting,filtering

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on the basis of name, age , height etc"), order : str = Query('ascending', description="query in ascending order optional")):

    load = p_data()
    valid_fields = ['age', 'bmi']
    order_type=["ascending", "descending"]
    # now from here error handling started
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400 , detail=f"invalid, pls select from {valid_fields}")
    
    if order not in order_type:
        raise HTTPException(status_code=400, detail=f"invalid, choose from {order_type}")
    sort_order = True if order == "descending" else False
    sorted_data=sorted(load.values(), key = lambda x: x.get(sort_by, 0), reverse=sort_order)

    

    return sorted_data

# so the url will be /sort?sort_by=age&order=descending

# also used f string that prints the value inside {}:ex:
# age = 24
# print(f"age is {age}") instead of print("age is ", age)
