from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from app import __version__, schemas
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
router = APIRouter()


@router.get("/get-countries", status_code=200)
async def get_all_countries():
    db = await get_database()
    collection = db["countries"]  # Specify your collection name
    countries_cursor = collection.find()
    countries = await countries_cursor.to_list(None)  # Fetch all documents
    # Convert _id from ObjectId to string for JSON serialization
    countries = [dict(country, _id=str(country["_id"])) for country in countries]
    # Use custom encoder for the response
    json_compatible_item_data = jsonable_encoder(countries, custom_encoder={ObjectId: str})
    return JSONResponse(content=json_compatible_item_data)