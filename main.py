from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Bike Marketplace"
)


fake_bikes = [
    {'id': 1, 'brand': 'Honda', 'model': "CBR600", "price": 5000},
    {'id': 2, 'brand': 'YAMAHA', 'model': "MT09 SP", "price": 7500},
    {'id': 3, 'brand': 'Kawasaki', 'model': "ZX6-R", "price": 3550.50},
]


class Bike(BaseModel):
    id: int
    brand: str
    model: str
    price: float = Field(ge=0)


@app.get('/bikes/{bike_id}', response_model=List[Bike])
def get_bike(bike_id: int):
    return [bike for bike in fake_bikes if bike.get('id') == bike_id]


@app.post('/bikes')
def add_bikes(bikes: List[Bike]):
    fake_bikes.extend(bikes)
    return {"status": 200, "data": fake_bikes}

