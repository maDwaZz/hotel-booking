from dataclasses import dataclass
from datetime import date

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

from app.bookings.router import router as router_bookings

app = FastAPI()

app.include_router(router_bookings)


@dataclass
class HotelSearchArgs:
    location: str
    date_from: date
    date_to: date
    has_spa: bool = None
    stars: int = Query(default=None, ge=1, le=5)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@app.get("/hotels", response_model=list[SHotel])
async def get_hotels(
        search_args: HotelSearchArgs = Depends()
):
    hotels = [
        {
            "address": "ул. Гагарина, 1, Алтай",
            "name": "Super Hotel",
            "stars": 5
        }
    ]
    return hotels


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
async def add_booking(booking: SBooking):
    pass


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
