from typing import List, Optional
from pydantic import BaseModel


class PriceChange(BaseModel):
    base: Optional[float] = None
    distance: Optional[float] = None
    duration: Optional[float] = None
    days_of_week: List[str]
    busy_hours: List[int]
    busy_hours_extra: Optional[float] = None
    week_day_extra: Optional[float] = None
    passenger_rating: Optional[float] = None
