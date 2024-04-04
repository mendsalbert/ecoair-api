import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_details: str = os.getenv('MONGO_DETAILS')
    database_name: str = "ecoair"
    collection_countries: str = "countries"
    collection_instruments: str = "instruments"
    collection_locations: str = 'locations'
    collection_parameters: str = 'parameters'
    collection_providers: str = 'providers'
    collection_owners: str = 'owners'
    collection_manufacturers: str = 'manufacturers'
    collection_sensors: str = "sensors"
    collection_sensors_by_loc_id : str = 'sensorsbylocid'

    class Config:
        env_file = '.env'

settings = Settings()
