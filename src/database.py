from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from os import environ

def opendb():
    db_url = environ.get("DATABASE_URL")
    if not db_url:
        raise EnvironmentError('Need to set a Postgres DATABASE_URL')
    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()