from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from app import __version__, schemas
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
router = APIRouter()


@router.get("/get-instruments", status_code=200)
async def get_all_instruments():
    db = await get_database()
    collection = db["instruments"]  # Specify your collection name
    instruments_cursor = collection.find()
    instruments = await instruments_cursor.to_list(None)  # Fetch all documents
    # Convert _id from ObjectId to string for JSON serialization
    instruments = [dict(instrument, _id=str(instrument["_id"])) for instrument in instruments]
    # Use custom encoder for the response
    json_compatible_item_data = jsonable_encoder(instruments, custom_encoder={ObjectId: str})
    return JSONResponse(content=json_compatible_item_data)