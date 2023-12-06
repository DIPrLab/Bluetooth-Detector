from aiohttp import ClientSession
from pytile import async_login

async def get_known_tiles(userdata: str) -> {}:
    tiles = {}
    async with ClientSession() as session:
        api = await async_login(userdata["tile_username"], userdata["tile_password"], session)
        tiles = await api.async_get_tiles()
    return tiles
