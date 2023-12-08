from typing import Any
import asyncio
from timeit import default_timer
import bleak
from bleak import BLEDevice
from pytile.tile import Tile

import config
import tile
from map import Geography


def time_to_seconds(time_hr: int = 0, time_min: int = 0, time_sec: int = 0) -> int:
    return (60 * ((time_hr * 60) + time_min)) + time_sec


async def look_for_devices(time_limit: int, percentage: int, interval: int = 5):
    device_list_per_interval: [set(bleak.BLEDevice)] = []
    results: set(BLEDevice) = set()
    start_time: float = default_timer()

    # Scan for devices (within given time frame) and add to list, divided by interval
    while (default_timer() - start_time) < time_limit:
        devices: list[BLEDevice] = await bleak.BleakScanner.discover(timeout=interval)
        device_list_per_interval.append(set(devices))

    # Add all scanned devices into set, without regard for time
    for devices in device_list_per_interval:
        for device in devices:
            results.add(device)

    # Print device info for all scanned devices
    print("Devices:")
    for d in results:
        print(d.name, d.address)
        print(d.details)
        print()


config: dict[str : str | dict[str:Any]] = config.get_config()
known_devices: dict[str:Tile] = asyncio.run(tile.get_known_tiles(config["user"]))
geo = Geography()
asyncio.run(look_for_devices(1, 90))
