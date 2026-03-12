from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import model, schemas, curd
from database import engine, SessionLocal, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employees/")
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)


@app.get("/employees/")
def read_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/employees/{emp_id}")
def read_employee(emp_id: int, db: Session = Depends(get_db)):
    return crud.get_employee(db, emp_id)


@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.update_employee(db, emp_id, employee)


@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db, emp_id)