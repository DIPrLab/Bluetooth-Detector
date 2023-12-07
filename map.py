from datetime import datetime
from typing import Any
import googlemaps


async def maps() -> None:
    gmaps: googlemaps.Client = await googlemaps.Client(
        key="AIzaSyDlMzYGce3b7aTDSsKNEvdXe7Qf7ouoHMI"
    )
    now: datetime = datetime.now()
    directions_result: Any = gmaps.directions(
        "", "", mode="transit", departure_time=now
    )
