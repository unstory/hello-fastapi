from datetime import datetime, date, timedelta

from sqlalchemy import create_engine, DateTime, Column

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from hello_fastapi.config import DevConfig

engine = create_engine(DevConfig.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class RawModel(Base):
    __abstract__ = True

    @classmethod
    def cols(cls, exclude=None):
        """
        获取所有字段
        :return:
        """
        if exclude is None:
            exclude = []
        columns = []
        for c in cls.__dict__:
            if isinstance(getattr(cls, c), Column) and c not in exclude:
                columns.append(c)
        return columns


class CoreModel(RawModel):
    __abstract__ = True
    CreateTime = Column(DateTime, default=datetime.now)
    UpdateTime = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def serialize(self, excludes=None):
        if excludes is None:
            excludes = []
        item = {}
        for c in self.cols(excludes):
            if isinstance(getattr(self, c.name), datetime):
                item[c.name] = (
                    getattr(self, c.name).strftime("%Y-%m-%d %H:%M:%S")
                    if getattr(self, c.name)
                    else None
                )
            elif isinstance(getattr(self, c.name), date):
                item[c.name] = (
                    getattr(self, c.name).strftime("%Y-%m-%d")
                    if getattr(self, c.name)
                    else None
                )
            else:
                item[c.name] = getattr(self, c.name, None)
        return item

    def cst_serialize(self, excludes=None):
        if excludes is None:
            excludes = []
        item = {}
        for c in self.cols(excludes):
            if isinstance(getattr(self, c.name), datetime):
                item[c.name] = (
                    (getattr(self, c.name) + timedelta(hours=8)).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                    if getattr(self, c.name)
                    else None
                )
            elif isinstance(getattr(self, c.name), date):
                item[c.name] = (
                    getattr(self, c.name).strftime("%Y-%m-%d")
                    if getattr(self, c.name)
                    else None
                )
            else:
                item[c.name] = getattr(self, c.name, None)
        return item


class BaseModel(CoreModel):
    __abstract__ = True
    DeleteTime = Column(DateTime, nullable=True)


if __name__ == "__main__":
    print(CoreModel.cols())
