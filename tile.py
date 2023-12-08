from aiohttp import ClientSession
from pytile import async_login
from pytile.tile import Tile
from pytile.api import API


async def get_known_tiles(userdata: str) -> dict[str:Tile]:
    tiles: dict[str:Tile] = {}
    async with ClientSession() as session:
        api: API = await async_login(
            userdata["tile_username"], userdata["tile_password"], session
        )
        tiles: dict[str:Tile] = await api.async_get_tiles()
    return tiles
