import tomllib
filename = 'config.toml'

with open(filename, 'rb') as f:
    cfg = tomllib.load(f)
