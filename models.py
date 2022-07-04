from sqlalchemy import Column, Integer, String

from database import Base


class Weapon(Base):
    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image_url = Column(String)


class Character(Base):
    __tablename__ = "game_character"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image_url = Column(String)
    

class Artifact(Base):
    __tablename__ = "artifact"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image_url = Column(String)