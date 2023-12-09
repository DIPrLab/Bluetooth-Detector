from timeit import default_timer
from datetime import datetime
from typing import Dict
from typing import TypeAlias
import bleak
from bleak import BLEDevice
from bleak import AdvertisementData

ScanMetadata: TypeAlias = Dict[str,  tuple[BLEDevice, AdvertisementData]]


class ScanData:
    def __init__(self, metadata: ScanMetadata) -> None:
        self.metadata: ScanMetadata = metadata
        self.time: datetime = datetime.now()


class Scanner:
    @staticmethod
    async def look_for_devices(
        time_limit: int, percentage: int, interval: int = 5
    ) -> list[ScanData]:
        result: list[BLEDevice] = list()
        start_time: float = default_timer()

        # Scan for devices (within given time frame) and add to list, divided by interval
        while (default_timer() - start_time) < time_limit:
            scan_result: ScanMetadata = await bleak.BleakScanner.discover(
                timeout=interval, return_adv=True
            )
            result.append(scan_result)

        return result
