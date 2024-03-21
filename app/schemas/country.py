from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field
class Parameter(BaseModel):
    id: int
    name: str
    units: str
    display_name: Optional[str] = Field(None, alias='displayName')

class Country(BaseModel):
    id: int
    code: str
    name: str
    datetime_first: str = Field(..., alias='datetimeFirst')
    datetime_last: str = Field(..., alias='datetimeLast')
    parameters: List[Parameter]

    class Config:
        allow_population_by_field_name = True
        extra = 'allow'

class CountriesResponse(BaseModel):
    results: List[Country]

    class Config:
        schema_extra = {
            "example": {
                "results": [
                    {
                        "id": 1,
                        "code": "NO",
                        "name": "Norway",
                        "datetimeFirst": "2016-12-02T10:00:00Z",
                        "datetimeLast": "2024-03-21T08:00:00Z",
                        "parameters": [
                            {"id": 1, "name": "pm10", "units": "µg/m³", "displayName": None},
                            {"id": 2, "name": "pm25", "units": "µg/m³", "displayName": None},
                            {"id": 3, "name": "o3", "units": "µg/m³", "displayName": None},
                            {"id": 4, "name": "co", "units": "µg/m³", "displayName": None},
                            {"id": 5, "name": "no2", "units": "µg/m³", "displayName": None},
                            {"id": 6, "name": "so2", "units": "µg/m³", "displayName": None},
                            {"id": 11, "name": "bc", "units": "µg/m³", "displayName": None},
                            {"id": 15, "name": "no2", "units": "ppb", "displayName": None},
                            {"id": 19, "name": "pm1", "units": "µg/m³", "displayName": None},
                            {"id": 21, "name": "co2", "units": "ppm", "displayName": None},
                            {"id": 24, "name": "no", "units": "ppb", "displayName": None},
                            {"id": 98, "name": "relativehumidity", "units": "%", "displayName": None},
                            {"id": 100, "name": "temperature", "units": "c", "displayName": None},
                            {"id": 125, "name": "um003", "units": "particles/cm³", "displayName": None},
                            {"id": 126, "name": "um010", "units": "particles/cm³", "displayName": None},
                            {"id": 128, "name": "temperature", "units": "f", "displayName": None},
                            {"id": 129, "name": "um050", "units": "particles/cm³", "displayName": None},
                            {"id": 130, "name": "um025", "units": "particles/cm³", "displayName": None},
                            {"id": 132, "name": "pressure", "units": "mb", "displayName": None},
                            {"id": 133, "name": "um005", "units": "particles/cm³", "displayName": None},
                            {"id": 134, "name": "humidity", "units": "%", "displayName": None},
                            {"id": 135, "name": "um100", "units": "particles/cm³", "displayName": None},
                            # ... add any additional parameters as needed ...
                        ]
                    }
                    # ... add more countries as needed ...
                ]
            }
        }
