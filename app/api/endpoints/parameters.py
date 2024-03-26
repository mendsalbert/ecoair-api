from fastapi import APIRouter, HTTPException
import httpx
from app.db.database import get_database
from app.core.config import settings
from app import __version__, schemas
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
router = APIRouter()

@router.get("/fetch_paramenters", status_code=200)
async def fetch_parameters():
    db = await get_database()
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.openaq.org/v3/parameters')
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Error fetching data from OpenAQ")
        data = response.json()
        if "results" in data:
            await db[settings.collection_parameters].insert_many(data["results"])
            return {"message": "Parameters data stored successfully in MongoDB."}
        else:
            return {"message": "No parameters data found."}


