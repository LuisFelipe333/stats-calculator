from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root:pokemon3@localhost:3306/game_objects"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
conn = engine.connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

meta = MetaData()

Base = declarative_base()
