
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse

app = FastAPI()

db = []
response_path = 'response.json'
class Garment(BaseModel):
    garment_type: str
    fabric: str
    size: str


@app.get('/')

def index():
    return {'key':'value'}


@app.get('/parameters')
def get_parameters():
    return db

# @app.get('/parameters/{parameter_id}')

# def get_parameter(parameter_id:int):
#     return db[parameter_id-1]


@app.get('/parameters/{garment_type}, {fabric}, {size}')

def get_all(garment_type:str, fabric:str, size:str):
    result = {'Garment Type':garment_type, 'Fabric': fabric, 'Size': size }
    return result

@app.post('/parameters')

def add_parameters(parameter: Garment):
    db.append(parameter.dict())
    return db[-1]

@app.delete('/parameters/{parameter_id}')
def delete_parameter(parameter_id:int):
    db.pop(parameter_id-1)
    return {}