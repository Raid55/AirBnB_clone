#!/usr/bin/python3
"""place class"""


class Place(BaseModel):
    """takes following as string"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    """takes following as int"""
    number_rooms = ""
    number_rooms = int(number_rooms)
    number_bathrooms = ""
    number_bathrooms = int(number_bathroom)
    max_guest = ""
    max_guest = int(max_guest)
    price_by_night = ""
    price_by_night = int(price_by_night)
    latitude = ""
    latitude = float(latitude)
    amentiy_ids[] = "" 
