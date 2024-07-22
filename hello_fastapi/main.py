from fastapi import FastAPI

from models.db import Base, engine

from api.router import init_router
# from api.organization.department import org_router

app = FastAPI()

init_router(app)
# Base.metadata.create_all(bind=engine)


# @org_router.get("/test", tags=["test"])
# def test():
#     return {"message": "Hello World"}


# app.include_router(org_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)
