from fastapi import APIRouter
from app.api.endpoints import countries, instruments, locations, parameters, providers, owners, manufacturers, sensors

api_router = APIRouter()

# Include routers from endpoints modules
api_router.include_router(countries.router, tags=["countries"], prefix="/countries")
# api_router.include_router(instruments.router, tags=["instruments"], prefix="/instruments")
# ... and so on for the other endpoint modules



# import json
# from typing import Any
# import asyncio
# import numpy as np
# import pandas as pd
# import os

# from fastapi import APIRouter, HTTPException, Depends
# from fastapi.encoders import jsonable_encoder
# from loguru import logger
# from regression_model import __version__ as model_version
# from regression_model.predict import make_prediction
# from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo.server_api import ServerApi
# from app import __version__, schemas
# from app.config import settings
# import httpx
# from dotenv import load_dotenv
# # from pathlib import Path

# from bson import ObjectId
# from fastapi.responses import JSONResponse

# api_router = APIRouter()
# load_dotenv()

# dotenv_path = Path('path/to/.env')
# load_dotenv(dotenv_path=dotenv_path)
# MONGO_DETAILS = os.getenv('MONGO_DETAILS')
# DATABASE_NAME = "ecoair"
# COLLECTION_COUNTRIES = "countries" 
# COLLECTION_INSTRUMENTS = "instruments" 
# COLLECTION_LOCATIONS = 'locations'
# COLLECTION_PARAMETERS = 'parameters'
# COLLECTION_PROVIDERS = 'providers'
# COLLECTION_OWNERS = 'owners'
# COLLECTION_MANUFACTURERS = 'manufacturers'
# COLLECTION_SENSORS = "sensors"

# GETSENSORSBYLOCATIONID 96

# class JSONEncoder(json.JSONEncoder):
#     """Extend json-encoder class"""
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)
    
# client = AsyncIOMotorClient(MONGO_DETAILS, server_api=ServerApi('1'))
# db = client[DATABASE_NAME]


# def get_database():
#     return db


# @api_router.get("/health", response_model=schemas.Health, status_code=200)
# def health() -> dict:
#     """
#     Root Get
#     """
#     health = schemas.Health(
#         name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
#     )

#     return health.dict()

# @api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
# async def predict(input_data: schemas.MultipleHouseDataInputs) -> Any:
#     """
#     Make house price predictions with the TID regression model
#     """

#     input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

#     # Advanced: You can improve performance of your API by rewriting the
#     # `make prediction` function to be async and using await here.
#     logger.info(f"Making prediction on inputs: {input_data.inputs}")
#     results = make_prediction(input_data=input_df.replace({np.nan: None}))

#     if results["errors"] is not None:
#         logger.warning(f"Prediction validation error: {results.get('errors')}")
#         raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

#     logger.info(f"Prediction results: {results.get('predictions')}")

#     return results

# @api_router.get("/fetch_countries")
# async def fetch_countries():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.openaq.org/v3/countries')
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
#         data = response.json()
#         if "results" in data:
#             await db[COLLECTION_COUNTRIES].insert_many(data["results"])
#             return {"message": "Countries data stored successfully in MongoDB."}
#         else:
#             return {"message": "No countries data found."}

# @api_router.get("/fetch_instruments")
# async def fetch_instruments():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.openaq.org/v3/instruments')
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
#         data = response.json()
#         if "results" in data:
#             await db[COLLECTION_INSTRUMENTS].insert_many(data["results"])
#             return {"message": "Instruments data stored successfully in MongoDB."}
#         else:
#             return {"message": "No instruments data found."}
        
# @api_router.get("/fetch_locations")
# async def fetch_locations():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.openaq.org/v3/locations')
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
#         data = response.json()
#         if "results" in data:
#             await db[COLLECTION_LOCATIONS].insert_many(data["results"])
#             return {"message": "Locations data stored successfully in MongoDB."}
#         else:
#             return {"message": "No locations data found."}
        
# @api_router.get("/fetch_parameters")
# async def fetch_parameters():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.openaq.org/v3/paramenters')
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
#         data = response.json()
#         if "results" in data:
#             await db[COLLECTION_PARAMETERS].insert_many(data["results"])
#             return {"message": "Parameters data stored successfully in MongoDB."}
#         else:
#             return {"message": "No parameters data found."}
        
# @api_router.get("/fetch_providers")
# async def fetch_providers():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.openaq.org/v3/providers')
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
#         data = response.json()
#         if "results" in data:
#             await db[COLLECTION_PROVIDERS].insert_many(data["results"])
#             return {"message": "Providers data stored successfully in MongoDB."}
#         else:
#             return {"message": "No providers data found."}
        
# @api_router.get("/fetch_owners")
# async def fetch_owners():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.openaq.org/v3/owners')
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
#         data = response.json()
#         if "results" in data:
#             await db[COLLECTION_OWNERS].insert_many(data["results"])
#             return {"message": "Owners data stored successfully in MongoDB."}
#         else:
#             return {"message": "No owners data found."}
        
# @api_router.get("/fetch_maufacturers")
# async def fetch_manufacturers():
#     async with httpx.AsyncClient() as client:
#         response = await client.get('https://api.openaq.org/v3/manufacturers')
#         if response.status_code != 200:
#             raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
#         data = response.json()
#         if "results" in data:
#             await db[COLLECTION_INSTRUMENTS].insert_many(data["results"])
#             return {"message": "Manufacturers data stored successfully in MongoDB."}
#         else:
#             return {"message": "No manufacturers data found."}

# @api_router.get("/locations", tags=["locations"])
# async def get_all_locations():
#     collection = db["locations"]  # Specify your collection name
#     locations_cursor = collection.find()
#     locations = await locations_cursor.to_list(None)  # Fetch all documents
#     # Convert _id from ObjectId to string for JSON serialization
#     locations = [dict(location, _id=str(location["_id"])) for location in locations]
#     # Use custom encoder for the response
#     json_compatible_item_data = jsonable_encoder(locations, custom_encoder={ObjectId: str})
#     return JSONResponse(content=json_compatible_item_data)
        
# @api_router.get("/fetch_sensors")
# async def fetch_sensors():
    async with httpx.AsyncClient() as client:
        # Fetch all locations
        response = await client.get('https://api.openaq.org/v3/locations')
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error fetching locations data from OpenAQ")

        locations_data = response.json()
        if "results" in locations_data:
            # For each location, fetch its sensors
            for location in locations_data["results"]:
                location_id = location["id"]  # Assuming 'id' is the correct key for location ID
                sensor_response = await client.get(f'https://api.openaq.org/v3/locations/{location_id}/sensors')
                
                if sensor_response.status_code == 200:
                    sensor_data = sensor_response.json()
                    if "results" in sensor_data and sensor_data["results"]:
                        # Insert sensor data into MongoDB
                        await db[COLLECTION_SENSORS].insert_many(sensor_data["results"])

            return {"message": "Sensors data stored successfully in MongoDB."}
        else:
            return {"message": "No locations data found."}