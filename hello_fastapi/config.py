from pathlib import Path

CURRENT_DIR = Path(__file__).parent


class DevConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/hello-fastapi?charset=utf8mb4'
