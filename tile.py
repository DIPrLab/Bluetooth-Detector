from aiohttp import ClientSession
from pytile import async_login

async def get_known_tiles(username: str, password: str) -> {}:
    tiles = {}
    async with ClientSession() as session:
        api = await async_login(username, password, session)
        tiles = await api.async_get_tiles()
    return tiles
