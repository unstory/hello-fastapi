from datetime import datetime

from sqlalchemy.orm import Session
from hello_fastapi.models.organization import Department


def create_department(db: Session, name: str, parent_id: int = None):
    db_department = Department(Name=name, ParentID=parent_id)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


def get_department(db: Session, department_id: int):
    return db.query(Department).filter(Department.id == department_id).first()


def get_departments(db: Session):
    return db.query(Department).filter(Department.DeleteTime.is_(None)).all()


def update_department(
    db: Session, department_id: int, name: str = None, parent_id: int = None
):
    db_department = get_department(db, department_id)
    if db_department is None:
        return None
    if name is not None:
        db_department.name = name
    if parent_id is not None:
        db_department.parent_id = parent_id
    db.commit()
    db.refresh(db_department)
    return db_department


def delete_department(db: Session, department_id: int):
    db_department = get_department(db, department_id)
    if db_department is None:
        return None
    if not db_department.delete_locked:
        # db.delete(db_department)
        db_department.DeleteTime = datetime.utcnow()
        db.commit()
        return db_department
    return None
