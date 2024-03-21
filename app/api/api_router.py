# app/api/api_router.py
from fastapi import APIRouter
from .endpoints.countries import router as countries_router
# import other routers from endpoints

api_router = APIRouter()
api_router.include_router(countries_router, prefix="/countries", tags=["Load Datasets"])
# include other routers similarly
