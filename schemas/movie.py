from typing import Optional
from pydantic import BaseModel, Field

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: int = Field(ge=1, le=10.0)
    category: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": 'pelicula',
                "overview": 'esta es la descripcion',
                "year": 2013,
                "rating": 5.0,
                "category": "Accion"
            }
        }