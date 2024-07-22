from fastapi import APIRouter, FastAPI

from hello_fastapi.api.organization.department import org_router

def init_router(app: FastAPI):
    app.include_router(org_router)