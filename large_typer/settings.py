from starlette.config import Config

import socket


def optional_str(v): return None if v is None else str(v)


config = Config()

DEBUG = config('API_DEBUG', cast=bool, default=False)
IP = config('API_IP', cast=str, default=socket.gethostbyname(socket.gethostname()))