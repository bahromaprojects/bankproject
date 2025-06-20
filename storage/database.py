from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.settings import db_settings

engine = create_engine(
    url=db_settings.db_url,
    echo=False,
)

session_factory = sessionmaker(engine)
