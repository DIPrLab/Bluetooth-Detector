import googlemaps
from datetime import datetime

async def maps() -> None:
    gmaps: googlemaps.Client = await googlemaps.Client(key="AIzaSyDlMzYGce3b7aTDSsKNEvdXe7Qf7ouoHMI")
    current_location = gmaps.geolocate()
    now = datetime.now()
    directions_result = gmaps.directions("", "", mode="transit", departure_time=now)