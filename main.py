import asyncio

from aiohttp import web
from routes import setup_routes
from db import setup_db

db = asyncio.run(setup_db())
app = web.Application()
app["db"] = db
setup_routes(app)
web.run_app(app)
