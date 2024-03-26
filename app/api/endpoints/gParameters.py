from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from app import __version__, schemas
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
router = APIRouter()


@router.get("/get-parameters", status_code=200)
async def get_all_parameters():
    db = await get_database()
    collection = db["parameters"]  # Specify your collection name
    parameters_cursor = collection.find()
    parameters = await parameters_cursor.to_list(None)  # Fetch all documents
    # Convert _id from ObjectId to string for JSON serialization
    parameters = [dict(parameter, _id=str(parameter["_id"])) for parameter in parameters]
    # Use custom encoder for the response
    json_compatible_item_data = jsonable_encoder(parameters, custom_encoder={ObjectId: str})
    return JSONResponse(content=json_compatible_item_data)