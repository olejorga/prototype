#   This is just a...
#    _____  _____   ____ _______ ____ _________     _______  ______
#   |  __ \|  __ \ / __ \__   __/ __ \__   __\ \   / /  __ \|  ____|
#   | |__) | |__) | |  | | | | | |  | | | |   \ \_/ /| |__) | |__
#   |  ___/|  _  /| |  | | | | | |  | | | |    \   / |  ___/|  __|
#   | |    | | \ \| |__| | | | | |__| | | |     | |  | |    | |____
#   |_|    |_|  \_\\____/  |_|  \____/  |_|     |_|  |_|    |______|
#
#   ...written with love in Python <3
#
#   Made by:
#       * Erik Teien Jarem
#       * Mujibullah Rahimi
#       * Ole-Jørgen Andersen
#       * Simen Jacobsen Øygard
#       * Sivert Østgård
#

# Importing FastAPI
from fastapi import FastAPI

# Importing routers
from .routers import items

# Initializing FastAPI...
app = FastAPI()

# Initializing routes...
app.include_router(items.router)
