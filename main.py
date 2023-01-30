from fastapi import FastAPI 
import db 
import models 

app = FastAPI() 

@app.get("/")
def root():
    return {"Hello": "My Name is Anvesh"}

@app.get("/all")
def get_all():
    data = db.all()
    return {"data":data}

@app.post("/create")
def create(data:models.Student):
    id = db.create(data)
    return {"inserted":True,"inserted_id":str(id)}

@app.get("/get/{name}")
def get_one(name: str):
    data = db.get_one(name)
    return {"Data": data}
