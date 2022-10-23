import datetime
import json
import random

from aiohttp import web
import db as db_utils
from bson import ObjectId


async def index(request):
    print(datetime.datetime.now())
    return web.Response(text="Hello, world")


async def get_all(request):
    db = request.app["db"]
    documents = await db_utils.do_find_many(db, 'sample_collection', {})

    return web.Response(body=json.dumps(documents), content_type="text/html")


async def get_one(request):
    db = request.app["db"]
    doc_id = request.match_info['doc_id']
    document = await db_utils.do_find_one(db, 'sample_collection', {'_id': ObjectId(doc_id)})
    document['_id'] = str(document['_id'])

    return web.Response(body=json.dumps(document), content_type="text/html")


async def add_data(request):
    db = request.app["db"]
    inserted_id = await db_utils.do_insert(db, 'sample_collection', {'key': random.random()})
    return web.Response(body=str(inserted_id), content_type="text/html")
