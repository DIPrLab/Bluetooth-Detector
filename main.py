from typing import Any
import asyncio
from pytile.tile import Tile

import config
import tile
from map import Geography

from scanner import ScanData
from scanner import Scanner

def time_to_seconds(time_hr: int = 0, time_min: int = 0, time_sec: int = 0) -> int:
    return (60 * ((time_hr * 60) + time_min)) + time_sec


geo = Geography()
config: dict[str : str | dict[str:Any]] = config.get_config()

known_devices: dict[str:Tile] = asyncio.run(tile.get_known_tiles(config["user"]))
scan_result: [ScanData] = asyncio.run(Scanner.look_for_devices(1, 90))

uuid: str
device: Tile
for uuid, device in known_devices.items():
    print(device.name)
    print(device.uuid)
    print()

uuid: str
for datum in scan_result:
    for uuid, (device, advertisement_data) in datum.items():
        print(device.name)
        print(uuid)
        print(advertisement_data)
        print()
