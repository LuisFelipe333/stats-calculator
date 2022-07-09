from pydantic import BaseModel

class WeaponBase(BaseModel):
    name:str
    image_url:str
    
class ArtifactBase(BaseModel):
    name:str
    image_url:str

class CharacterBase(BaseModel):
    name:str
    image_url:str

class StatisticBase(BaseModel):
    name:str

class Weapon(WeaponBase):
    id:int
    class Config:
        orm_mode = True

class Artifact(ArtifactBase):
    id:int
    class Config:
        orm_mode = True
        
class Character(CharacterBase):
    id:int
    class Config:
        orm_mode = True

class Statistic(StatisticBase):
    id:int
    class Config:
        orm_mode = True