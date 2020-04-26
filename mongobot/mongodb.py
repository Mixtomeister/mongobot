import os, urllib, importlib
from pymodm.connection import connect
from telegram.ext import CommandHandler
from mongobot.models import Command

def new_connection():
    user = urllib.parse.quote(os.environ.get("MONGO_ROOT_USER"))
    password = urllib.parse.quote(os.environ.get("MONGO_ROOT_PASSWORD"))
    db = os.environ.get("MONGO_INIT_DATABASE")
    connect(f"mongodb://{user}:{password}@mongo:27017/{db}?authSource=admin", alias="mongobot")

def load_commands(dispatcher):
    for c in Command.objects.all():
        p, m = c.handler.rsplit('.', 1)
        pkg = importlib.import_module(p)
        handler = getattr(pkg, m)
        dispatcher.add_handler(CommandHandler(c.command, handler))