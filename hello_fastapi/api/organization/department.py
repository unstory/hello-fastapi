from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse

from hello_fastapi.models.db import get_db

from hello_fastapi.crud.organization.department import (
    create_department,
    get_department,
    get_departments,
    update_department,
    delete_department,
)
from hello_fastapi.schema.organization.department import DepartmentResponse

org_router = APIRouter(prefix="/org")


@org_router.post(
    "/", response_model=DepartmentResponse, responses={200: {"payload": DepartmentResponse, "msg": "ok", "code": 0}}, tags=["department"], summary="创建部门"
)
def post_department(name: str, parent_id: int = None, db: Session = Depends(get_db)):
    new_department = create_department(db, name, parent_id)
    department = DepartmentResponse(**new_department.serialize())
    return department


@org_router.get(
    "/", tags=["department"], summary="查询部门列表"
)
def get_departments(db: Session = Depends(get_db)):
    department_lst = get_departments(db)
    result = [department.serialize() for department in department_lst]
    return JSONResponse(content=result, status_code=200)


@org_router.get(
    "/{department_id}",
    tags=["department"],
    summary="查询部门",
)
def get_department(department_id: int, db: Session = Depends(get_db)):
    department = get_department(db, department_id)
    return JSONResponse(content=department.serialize(), status_code=200)


@org_router.put(
    "/{department_id}",
    tags=["department"],
    summary="更新部门",
)
def put_department(
    department_id: int,
    name: str = None,
    parent_id: int = None,
    db: Session = Depends(get_db),
):
    department = update_department(db, department_id, name, parent_id)
    return JSONResponse(content=department.serialize(), status_code=200)


@org_router.delete(
    "/{department_id}",
    tags=["department"],
    summary="删除部门",
)
def del_department(department_id: int, db: Session = Depends(get_db)):
    department = delete_department(db, department_id)
    return JSONResponse(content=department.serialize(), status_code=200)


# @org_router.post(
#     "/", tags=["department"], summary="创建部门"
# )
# def post_department(name: str, parent_id: int = None, db: Session = Depends(get_db)):
#     department = create_department(db, name, parent_id)
#     return JSONResponse(content=department.serialize(), status_code=201)
