from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    salary: int


class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True