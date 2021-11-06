from flask import Flask
from babel.dates import format_timedelta as td
import jinja2
from datetime import datetime, timedelta

from sqlalchemy.sql.type_api import STRINGTYPE

app = Flask(__name__)

def format_post_age(value):
    format = "%Y-%m-%d %H:%M:%S.%f"
    seconds=datetime.now() - datetime.strptime(str(value), format)
    return td(seconds)

jinja2.filters.FILTERS['format_post_age'] = format_post_age