from sqlalchemy.orm import Session

import models

class Operations:
    
    def get_characters(db:Session, skip:int = 0, limit:int = 200):
        return db.query(models.Character).offset(skip).limit(limit).all()

    def get_weapons(db:Session, skip:int = 0, limit:int = 200):
        return db.query(models.Weapon).offset(skip).limit(limit).all()

    def get_artifacts(db:Session, skip:int = 0, limit:int = 200):
        return db.query(models.Artifact).offset(skip).limit(limit).all()


