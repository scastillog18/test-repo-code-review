import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-in-prod")
    DATABASE = os.environ.get("DATABASE_PATH", "taskflow.db")
    TESTING = False


class TestingConfig(Config):
    TESTING = True
    DATABASE = ":memory:"


configs = {
    "development": Config,
    "testing": TestingConfig,
    "default": Config,
}
