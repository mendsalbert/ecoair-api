from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from app import __version__, schemas
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
router = APIRouter()


@router.get("/get-providers", status_code=200)
async def get_all_providers():
    db = await get_database()
    collection = db["providers"]  # Specify your collection name
    providers_cursor = collection.find()
    providers = await providers_cursor.to_list(None)  # Fetch all documents
    # Convert _id from ObjectId to string for JSON serialization
    providers = [dict(provider, _id=str(provider["_id"])) for provider in providers]
    # Use custom encoder for the response
    json_compatible_item_data = jsonable_encoder(providers, custom_encoder={ObjectId: str})
    return JSONResponse(content=json_compatible_item_data)