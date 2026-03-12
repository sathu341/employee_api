from sqlalchemy.orm import Session
import model, schemas


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    emp = models.Employee(**employee.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


def get_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeCreate):

    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    if emp:
        emp.name = employee.name
        emp.email = employee.email
        emp.department = employee.department
        emp.salary = employee.salary

        db.commit()
        db.refresh(emp)

    return emp


def delete_employee(db: Session, emp_id: int):

    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    if emp:
        db.delete(emp)
        db.commit()

    return emp