import certifi
import pytz
from datetime import timedelta, datetime
import os
from loguru import logger
from pathlib import Path
import pymongo
from pydantic import ConfigDict
from starlette.config import Config

BASE_DIR = Path(__file__).resolve().parent.parent
logger.warning(f"basedir: {BASE_DIR}")

config = Config(os.path.join(BASE_DIR, ".env"))
MONGODB_URI = config("MONGODB_URI")
GREY_AUTH_TOKEN = config("GREY_AUTH_TOKEN")

def datetime_now():
    return datetime.now(tz=pytz.UTC)


def create_dir(*name):
    """For creating recursive and non-recursive directories ."""
    fullpath = os.path.join(BASE_DIR, *name)
    os.makedirs(fullpath, exist_ok=True)
    return fullpath


simple_pydantic_model_config = ConfigDict(
    str_strip_whitespace=True,
    use_enum_values=True,
    populate_by_name=True,
)

client = pymongo.MongoClient(str(MONGODB_URI), tlsCAFile=certifi.where())
db = client["nairalog"]
