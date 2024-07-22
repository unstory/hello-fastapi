from datetime import datetime

from pydantic import BaseModel, ValidationError


class MyCoreModel(BaseModel):
    CreateTime: datetime
    UpdateTime: datetime

class MyBaseModel(MyCoreModel):
    DeleteTime: datetime | None


class DepartmentResponse(MyBaseModel):
    id: int
    Name: str
    ParentID: int
    IsUsable: bool

    class Config:
        orm_model = True
