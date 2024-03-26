from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from app import __version__, schemas
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
router = APIRouter()


@router.get("/get-locations",response_model=schemas.LocationResponse, status_code=200)
async def get_all_locations():
    db = await get_database()
    collection = db["locations"]  # Specify your collection name
    locations_cursor = collection.find()
    locations = await locations_cursor.to_list(None)  # Fetch all documents
    # Convert _id from ObjectId to string for JSON serialization
    locations = [dict(location, _id=str(location["_id"])) for location in locations]
    # Use custom encoder for the response
    json_compatible_item_data = jsonable_encoder(locations, custom_encoder={ObjectId: str})
    return JSONResponse(content=json_compatible_item_data)