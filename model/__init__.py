from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .category import Category
from .news import News
