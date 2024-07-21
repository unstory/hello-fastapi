from hello_fastapi.models.db import BaseModel

from sqlalchemy import Column, Integer, String, Boolean


class User(BaseModel):
    __tablename__ = "org_user"
    id = Column(Integer, doc="自增主键ID", primary_key=True, autoincrement=True)
    NickName = Column(String(255), doc="中文名", nullable=False)
    ZhName = Column(String(255), doc="昵称", default="")
    Email = Column(String(255), doc="邮箱", nullable=False)
    Phone = Column(String(11), doc="手机号", default="")
    DepartmentID = Column(Integer, doc="部门ID", default=0)
    Password = Column(String(255), doc="加密后的密码", nullable=False)
    IsUsable = Column(Boolean, doc="是否可用", default=True)

    def serialize(self, excludes=None):
        if excludes is None:
            excludes = ["Password"]
        return super().serialize(excludes)


class Department(BaseModel):
    __tablename__ = "org_department"
    id = Column(Integer, doc="自增主键ID", primary_key=True, autoincrement=True)
    Name = Column(String(255), doc="部门名称", nullable=False)
    ParentID = Column(Integer, doc="父部门ID", default=0)
    IsUsable = Column(Boolean, doc="是否可用", default=True)

    @classmethod
    def delete_locked(cls):
        count = cls.query.filter(
            Department.id == cls.ParentID,
            Department.IsUsable.is_(True),
            Department.DeleteTime.is_(None),
        )
        return count > 0
