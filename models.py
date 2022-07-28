from sqlalchemy import Column, Integer, String, Float,Table

from database import Base, meta, engine


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
    
class Statistic(Base):
    __tablename__ = "statistics"
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    
class CharacterStatistics(Base):
    __tablename__ = "character_statistics"
    id = Column(Integer, primary_key = True, index=True)
    base_hp =  Column(Integer)
    base_atk =  Column(Integer)
    base_def =  Column(Integer)
    extra_stat =  Column(Integer)
    extra_stat_value =  Column(Float)
    element =  Column(Integer)
    talent1_damage =  Column(Float)
    talent2_damage =  Column(Float)
    talent3_damage =  Column(Float)
    
characterTable = Table(
    "character_statistics", 
    meta,
    Column("id", Integer, primary_key = True),
    Column("base_hp", Integer),
    Column("base_atk", Integer),
    Column("base_def", Integer),
    Column("extra_stat", Integer),
    Column("extra_stat_value", Float),
    Column("element", Integer),
    Column("talent1_damage", Float),
    Column("talent2_damage", Float),
    Column("talent3_damage", Float),
)

character = Table(
    "game_character",
    meta,
    Column("id",Integer, primary_key=True),
    Column("name",String(255)),
    Column("image_url",String(255)),
)


meta.create_all(engine)