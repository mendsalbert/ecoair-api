from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field

class Coordinates(BaseModel):
    latitude: float
    longitude: float

class Sensor(BaseModel):
    id: str
    name: str
    # Define other fields based on the sensor details you expect

class Instrument(BaseModel):
    id: str
    name: str
    # Define other fields based on the instrument details you expect

class Country(BaseModel):
    code: str
    name: str

class Owner(BaseModel):
    name: str
    # Define other fields based on the owner details you expect

class Provider(BaseModel):
    name: str
    # Define other fields based on the provider details you expect

class DateTimeInfo(BaseModel):
    datetime: str
    timezone: str

class Location(BaseModel):
    id: Union[str, int]  # ID might be str or int
    name: str
    locality: Optional[str]
    timezone: str
    country: Optional[Country]
    owner: Optional[Owner]
    provider: Optional[Provider]
    is_mobile: Optional[bool] = Field(default=False, alias='isMobile')
    is_monitor: Optional[bool] = Field(default=True, alias='isMonitor')
    instruments: Optional[List[Instrument]]
    sensors: Optional[List[Sensor]]
    coordinates: Optional[Coordinates]
    licenses: Optional[Any]
    bounds: Optional[List[Any]]
    distance: Optional[Any]
    datetime_first: Optional[DateTimeInfo] = Field(alias='datetimeFirst')
    datetime_last: Optional[DateTimeInfo] = Field(alias='datetimeLast')

    class Config:
        allow_population_by_field_name = True

class CountriesResponse(BaseModel):
    results: List[Location]

    class Config:
        schema_extra = {
            "example": {
                "results": [
                    {
                        "id": "65fb1a5b67035054625a387b",
                        "name": "Delhi Technological University, Delhi - CPCB",
                        "timezone": "Asia/Kolkata",
                        "country": {"code": "IN", "name": "India"},
                        "owner": {"name": "CPCB"},
                        "provider": {"name": "Provider Name"},
                        "isMobile": False,
                        "isMonitor": True,
                        "instruments": [{"id": "1", "name": "Instrument Name"}],
                        "sensors": [
                            {"id": "1", "name": "Sensor 1"},
                            {"id": "2", "name": "Sensor 2"}
                        ],
                        "coordinates": {"latitude": 28.7501, "longitude": 77.1177},
                        "datetimeFirst": {"datetime": "2021-01-01T00:00:00Z", "timezone": "UTC"},
                        "datetimeLast": {"datetime": "2021-01-02T00:00:00Z", "timezone": "UTC"},
                        # ... other fields ...
                    }
                ]
            }
        }
