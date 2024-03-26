# app/api/api_router.py
from fastapi import APIRouter
from .endpoints.countries import router as countries_router
# import other routers from endpoints
from .endpoints import (
    countries,
    # instruments,
    locations,
    gLocations,
    parameters,
    gParameters
    # parameters,
    # providers,
    # owners,
    # manufacturers,
    # sensors
)
api_router = APIRouter()
api_router.include_router(countries.router, prefix="/countries", tags=["Load Datasets"])
api_router.include_router(locations.router, prefix="/locations", tags=["Load Datasets"])
api_router.include_router(parameters.router, prefix="/parameters", tags=["Load Datasets"])


api_router.include_router(gLocations.router, prefix="/locations", tags=["Get Datasets"])
api_router.include_router(gParameters.router, prefix="/parameters", tags=["Get Datasets"])
# api_router.include_router(locations.router, prefix="/locations", tags=["Locations"])
# include other routers similarly
