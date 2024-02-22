import os

DEBUG = True

SECRET_KEY = os.urandom(32)

SQLALCHEMY_DATABASE_URI = (
    "postgresql://api_admin:1234@localhost:5432/fast_food_restaurant"
)
SQLALCHEMY_TRACK_MODIFICATIONS = True
