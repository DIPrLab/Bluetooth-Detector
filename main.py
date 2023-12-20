from typing import Any
import asyncio
from pytile.tile import Tile

from bleak import AdvertisementData
from bleak import BLEDevice
import config
import tile
from map import Geography

from scanner import ScanData
from scanner import Scanner


def time_to_seconds(time_hr: int = 0, time_min: int = 0, time_sec: int = 0) -> int:
    return (60 * ((time_hr * 60) + time_min)) + time_sec


geo = Geography()
config: dict[str: str | dict[str:Any]] = config.get_config()

known_devices: dict[str:Tile] = asyncio.run(
    tile.get_known_tiles(config["user"]))

uuid: str
tile_tag: Tile
for uuid, tile_tag in known_devices.items():
    print(tile_tag.name)
    print(tile_tag.uuid)
    print()

scan_result:[ScanData] = asyncio.run(Scanner.look_for_devices(30, 90))
scan_result = set(scan_result)

uuid: str
datum: ScanData
device: BLEDevice
advertisement_data: AdvertisementData
for datum in scan_result:
    for uuid, (device, advertisement_data) in datum.metadata.items():
        print(device.name)
        print(uuid)
        print(advertisement_data)
        print(advertisement_data.service_data)
        # print(advertisement_data.platform_data)
        print()
