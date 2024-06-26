# app/api/api_router.py
from fastapi import APIRouter
from .endpoints.countries import router as countries_router
# import other routers from endpoints
from .endpoints import (
    countries,
    locations,
    parameters,
    manufacturers,
    providers,
    instruments,
    sensorsByLocation,
    gLocations,
    gParameters,
    gCountries,
    gManufacturers,
    gProviders,
    gIntruments
    
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
api_router.include_router(manufacturers.router, prefix="/manufacturers", tags=["Load Datasets"])
api_router.include_router(providers.router, prefix="/providers", tags=["Load Datasets"])
api_router.include_router(instruments.router, prefix="/instruments", tags=["Load Datasets"])
api_router.include_router(sensorsByLocation.router, prefix="/sensors-by-location", tags=["Load Datasets"])


api_router.include_router(gLocations.router, prefix="/locations", tags=["Get Datasets"])
api_router.include_router(gParameters.router, prefix="/parameters", tags=["Get Datasets"])
api_router.include_router(gCountries.router, prefix="/countries", tags=["Get Datasets"])
api_router.include_router(gManufacturers.router, prefix="/manufacturers", tags=["Get Datasets"])
api_router.include_router(gProviders.router, prefix="/providers", tags=["Get Datasets"])
api_router.include_router(gIntruments.router, prefix="/instruments", tags=["Get Datasets"])
