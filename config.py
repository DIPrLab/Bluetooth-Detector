import tomllib

def get_config() -> dict():
    config = {}
    with open("config.toml", "rb") as file:
        config = tomllib.load(file)
    return config
