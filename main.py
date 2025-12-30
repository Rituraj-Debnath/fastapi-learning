from fastapi import FastAPI

obj = FastAPI()

@obj.get("/about")

def practice_api():
    return{"name": "Rituraj Debnath", 
           "age": "24"}