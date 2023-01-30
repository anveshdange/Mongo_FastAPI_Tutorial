from pydantic import BaseModel 

class Student(BaseModel):
    name: str 
    ph : str 
    father: str 
    mother: str 
    fatherPH:str 
    motherPH:str 
    dob:str 
    