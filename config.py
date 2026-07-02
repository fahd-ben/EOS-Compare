import os
from dotenv import load_dotenv

load_dotenv()

# Neon / Supabase / Heroku renvoient parfois "postgres://" au lieu de
# "postgresql://", ce que SQLAlchemy 2.x n'accepte plus tel quel.
_raw_db_url = os.getenv("DATABASE_URL", "")
if _raw_db_url.startswith("postgres://"):
    _raw_db_url = _raw_db_url.replace("postgres://", "postgresql://", 1)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "eos-compare-dev-secret")
    # SQLite par defaut (developpement local), Postgres en production
    SQLALCHEMY_DATABASE_URI = _raw_db_url or "sqlite:///eos_compare.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv("DEBUG", "True") == "True"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///eos_compare.db"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = _raw_db_url


config = {
    "development": DevelopmentConfig,
    "production":  ProductionConfig,
    "default":     DevelopmentConfig,
}
