from sqlalchemy.orm import Session
from fastapi import Depends

from . import org_router

from hello_fastapi.models.db import get_db

from hello_fastapi.models.organization import Department
from hello_fastapi.crud.organization.department import (
    create_department,
    get_department,
    get_departments,
    update_department,
    delete_department,
)


@org_router.post("/", response_model=Department, tags=["department"], summary="创建部门")
def post_department(name: str, parent_id: int = None, db: Session = Depends(get_db)):
    return create_department(db, name, parent_id)


@org_router.get("/", response_model=list[Department], tags=["department"], summary="查询部门列表")
def get_departments(db: Session = Depends(get_db)):
    return get_departments(db)
