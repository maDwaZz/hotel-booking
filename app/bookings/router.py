from fastapi import APIRouter

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("", response_model=list[SBooking])
async def get_bookings():
    return await BookingDAO.find_all()


@router.get("/{booking_id}")
async def get_booking(booking_id: int):
    return await BookingDAO.find_by_id(booking_id)
