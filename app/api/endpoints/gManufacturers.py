from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from app import __version__, schemas
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
router = APIRouter()


@router.get("/get-manufacturers", status_code=200)
async def get_all_manufacturers():
    db = await get_database()
    collection = db["manufacturers"]  # Specify your collection name
    manufacturers_cursor = collection.find()
    manufacturers = await manufacturers_cursor.to_list(None)  # Fetch all documents
    # Convert _id from ObjectId to string for JSON serialization
    manufacturers = [dict(manufacturer, _id=str(manufacturer["_id"])) for manufacturer in manufacturers]
    # Use custom encoder for the response
    json_compatible_item_data = jsonable_encoder(manufacturers, custom_encoder={ObjectId: str})
    return JSONResponse(content=json_compatible_item_data)