from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/fetch_sensors_for_locations", status_code=200)
async def fetch_sensors_for_locations():
    db = await get_database()
    async with httpx.AsyncClient() as client:
        locations_response = await client.get('https://api.openaq.org/v3/locations')
        
        if locations_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error fetching locations data from OpenAQ")
        
        locations_data = locations_response.json()
        if "results" not in locations_data:
            return {"message": "No locations data found."}

        for location in locations_data["results"]:
            location_id = location["id"]
            
            # Skip the location with ID 13
            if location_id == 13:
                print(f"Skipping location ID {location_id} as per instructions.")
                continue
            
            sensors_response = await client.get(f'https://api.openaq.org/v3/locations/{location_id}/sensors')
            
            if sensors_response.status_code != 200:
                print(f"Error fetching sensors data for location ID {location_id} from OpenAQ: {sensors_response.status_code}")
                continue  # Skip to the next location in case of error
            
            sensors_data = sensors_response.json()
            if "results" in sensors_data:
                sensor_documents = [{
                    'sensor_id': sensor['id'],
                    'name': sensor['name'],
                    'parameter': sensor['parameter'],
                    'datetimeFirst': sensor.get('datetimeFirst', {}).get('utc'),
                    'datetimeLast': sensor.get('datetimeLast', {}).get('utc'),
                    # include any other fields you want to store
                } for sensor in sensors_data["results"]]

                # Insert or update the sensor data for this location
                await db[settings.collection_sensors_by_loc_id].update_one(
                    {"location_id": location_id},
                    {"$set": {"sensors": sensor_documents}},
                    upsert=True
                )
                
        return JSONResponse(content={"message": "Sensors data stored successfully for all locations, with location ID 13 skipped."})
