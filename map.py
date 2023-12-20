from datetime import datetime
from typing import Any
import googlemaps
# import geocoder


class Geography:
    def __init__(self) -> None:
        self.gmaps_key: str = "AIzaSyDlMzYGce3b7aTDSsKNEvdXe7Qf7ouoHMI"
        self.gmaps: googlemaps.Client = googlemaps.Client(key=self.gmaps_key)

    async def maps(self) -> None:
        now: datetime = datetime.now()
        directions_result: Any = self.gmaps.directions(
            "", "", mode="transit", departure_time=now
        )

    # def get_user_location(self) -> dict[str:Any]:
    #     geo: dict[str:Any] = geocoder.ip("me")
    #     return geo
