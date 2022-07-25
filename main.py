from distutils.log import debug
from matplotlib.pyplot import title
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal
from operations import Operations
import schemas
from modelChar import CharRequestModel

app= FastAPI(title="Statistics calculator",
             description= "Calculate the stats of the characters based on their weapon and artifacts",
             version="1.0.0")

@app.get('/')
def index():
    return "a"

@app.post('/char')
def calculate_char(char: CharRequestModel):
    
    return calculate_stats(char)

def calculate_stats(char: CharRequestModel):
    statics_to_add=[0]*20
    hp=char.base_hp
    atk=char.base_atk+char.weapon_atk_base
    defense=char.base_def
    em=char.base_em
    ctr=char.base_ctr
    ctd=char.base_ctd
    healing_bonus=char.healing_bonus_base
    energy_recharge=char.energy_recharge_base
    pyro_dmg=char.pyro_dmg_base
    hydro_dmg=char.hydro_dmg_base
    electro_dmg=char.electro_dmg_base
    anemo_dmg=char.anemo_dmg_base
    cryo_dmg=char.cryo_dmg_base
    geo_dmg=char.geo_dmg_base
    dendro_dmg=char.dendro_dmg_base
    phys_dmg=char.phys_dmg_base
    
    
    if(char.art1_type!=0):
        if(char.art1_main_stat!=0):
            statics_to_add[char.art1_main_stat]+=char.art1_main_stat_value
        if(char.art1_stat1!=0):
            statics_to_add[char.art1_stat1]+=char.art1_stat1_value
        if(char.art1_stat2!=0):
            statics_to_add[char.art1_stat2]+=char.art1_stat2_value
        if(char.art1_stat3!=0):
            statics_to_add[char.art1_stat3]+=char.art1_stat3_value
        if(char.art1_stat4!=0):
            statics_to_add[char.art1_stat4]+=char.art1_stat4_value
            
    if(char.art2_type!=0):
        if(char.art2_main_stat!=0):
            statics_to_add[char.art2_main_stat]+=char.art2_main_stat_value
        if(char.art2_stat1!=0):
            statics_to_add[char.art2_stat1]+=char.art2_stat1_value
        if(char.art2_stat2!=0):
            statics_to_add[char.art2_stat2]+=char.art2_stat2_value
        if(char.art2_stat3!=0):
            statics_to_add[char.art2_stat3]+=char.art2_stat3_value
        if(char.art2_stat4!=0):
            statics_to_add[char.art2_stat4]+=char.art2_stat4_value
    
    if(char.art3_type!=0):
        if(char.art3_main_stat!=0):
            statics_to_add[char.art3_main_stat]+=char.art3_main_stat_value
        if(char.art3_stat1!=0):
            statics_to_add[char.art3_stat1]+=char.art3_stat1_value
        if(char.art3_stat2!=0):
            statics_to_add[char.art3_stat2]+=char.art3_stat2_value
        if(char.art3_stat3!=0):
            statics_to_add[char.art3_stat3]+=char.art3_stat3_value
        if(char.art3_stat4!=0):
            statics_to_add[char.art3_stat4]+=char.art3_stat4_value
    
    if(char.art4_type!=0):
        if(char.art4_main_stat!=0):
            statics_to_add[char.art4_main_stat]+=char.art4_main_stat_value
        if(char.art4_stat1!=0):
            statics_to_add[char.art4_stat1]+=char.art4_stat1_value
        if(char.art4_stat2!=0):
            statics_to_add[char.art4_stat2]+=char.art4_stat2_value
        if(char.art4_stat3!=0):
            statics_to_add[char.art4_stat3]+=char.art4_stat3_value
        if(char.art4_stat4!=0):
            statics_to_add[char.art4_stat4]+=char.art4_stat4_value
    
    hp=hp*(1+(statics_to_add[2]/100))
    hp=hp+statics_to_add[1]
    
    atk=atk*(1+(statics_to_add[4]/100))
    atk=atk+statics_to_add[3]
    
    print(statics_to_add[5])
    print(statics_to_add[6])
    defense=defense*(1+(statics_to_add[6]/100))
    defense=defense+statics_to_add[5]
    em=em+statics_to_add[7]
    ctr=ctr+statics_to_add[8]
    ctd=ctd+statics_to_add[9]
    healing_bonus=healing_bonus+statics_to_add[10]
    energy_recharge=energy_recharge+statics_to_add[11]
    pyro_dmg=pyro_dmg+statics_to_add[12]
    hydro_dmg=hydro_dmg+statics_to_add[13]
    electro_dmg=electro_dmg+statics_to_add[14]
    anemo_dmg=anemo_dmg+statics_to_add[15]
    cryo_dmg=cryo_dmg+statics_to_add[16]
    geo_dmg=geo_dmg+statics_to_add[17]
    dendro_dmg=dendro_dmg+statics_to_add[18]
    phys_dmg=phys_dmg+statics_to_add[19]
    
    #obtener los datos de talentos y elemento del personaje


    element=0
    base_stat=[1,1,1]
    talent_damage=[100,8.77,8.77]
    
    #en base al tipo de artefacto obtengo los bonus extras
    
    ult_bonus=20  
    
    
    
    # stats for talent damage
    # "hp": 0
    # "atk": 1
    # "def": 2
    # "em": 3
    # "healing_bonus": 4
    # "energy_recharge": 5

    #damage arrays
    prom_damage = [0]*3
    normal_damage = [0]*3
    crit_damage = [0]*3


    #damage calculatin start
    talent_damage_base=[0]*3
    for i in range (3):
        talent_damage_base[i]=atk*(talent_damage[i]/100)
    print(talent_damage[1])
    print(talent_damage_base[1])   
    bonus_damage=0
    # if(char.talentNumber==2):
    #     bonus_damage+=char.ult_bonus/100
        
        
    if(element==0):
        bonus_damage+=pyro_dmg/100
    elif(element==1):
        bonus_damage+=hydro_dmg/100
    elif(element==2):
        bonus_damage+=electro_dmg/100
    elif(element==3):
        bonus_damage+=anemo_dmg/100
    elif(element==4):
        bonus_damage+=cryo_dmg/100
    elif(element==5):
        bonus_damage+=geo_dmg/100
    elif(element==6):
        bonus_damage+=dendro_dmg/100
    elif(element==7):
        bonus_damage+=phys_dmg/100
      
    talent_crit_damage=[0]*3    
    talent_prom_damage=[0]*3
    
    for i in range (3):
        if(i==2):
            talent_damage_base[i]=talent_damage_base[i]*(1+(bonus_damage+ult_bonus))
        elif(i==0):
            talent_damage_base[i]=talent_damage_base[i]*(1+bonus_damage)
        
        talent_crit_damage[i]=talent_damage_base[i]*(1+(ctd/100))
        talent_prom_damage[i]=talent_damage_base[i]*(1+((ctd/100)*(ctr/100)))
        
    
        
    
        
    
    statics_json={
        "hp": hp,
        "atk": atk,
        "def": defense,
        "em": em,
        "ctr": ctr,
        "ctd": ctd,
        "healing_bonus": healing_bonus,
        "energy_recharge": energy_recharge,
        "pyro_dmg": pyro_dmg,
        "hydro_dmg": hydro_dmg,
        "electro_dmg": electro_dmg,
        "anemo_dmg": anemo_dmg,
        "cryo_dmg": cryo_dmg,
        "geo_dmg": geo_dmg,
        "dendro_dmg": dendro_dmg,
        "phys_dmg": phys_dmg,
        "talent1_normal_damage": talent_damage_base[0],
        "talent1_crit_damage": talent_crit_damage[0],
        "talent1_prom_damage": talent_prom_damage[0],
        "talent2_normal_damage": talent_damage_base[1],
        "talent2_crit_damage": talent_crit_damage[1],
        "talent2_prom_damage": talent_prom_damage[1],
        "talent3_normal_damage": talent_damage_base[2],
        "talent3_crit_damage": talent_crit_damage[2],
        "talent3_prom_damage": talent_prom_damage[2],
    }
    
    return statics_json


#CHARACTER
# "hp": 0
# "atk": 1
# "def": 2
# "em": 3
# "ctr": 4
# "ctd": 5
# "healing_bonus": 6
# "energy_recharge": 7
# "pyro_dmg": 8
# "hydro_dmg": 9
# "electro_dmg": 10
# "anemo_dmg": 11
# "cryo_dmg": 12
# "geo_dmg": 13
# "dendro_dmg": 14
# "phys_dmg": 15

#ARTIFACTS
# flat_hp:1
# per_hp:2
# flat_atk: 3
# per_atk: 4
# flat_def: 5
# per_def: 6
# elemental mastery: 7
# ctr: 8
# ctd: 9
# healing_bonus:10
# energy_recharge:11
# pyro_dmg:12
# hydro_dmg:13
# electro_dmg:14
# anemo_dmg:15
# cryo_dmg:16
# geo_dmg:17
# dendro_dmg:18
# phys_dmg:19


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/get_characters', response_model=list[schemas.Character])
def get_characters(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    items = Operations.get_characters(db, skip=skip, limit=limit)
    return items

@app.get('/get_weapons', response_model=list[schemas.Weapon])
def get_characters(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    items = Operations.get_weapons(db, skip=skip, limit=limit)
    return items

@app.get('/get_artifacts', response_model=list[schemas.Artifact])
def get_characters(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    items = Operations.get_artifacts(db, skip=skip, limit=limit)
    return items

@app.get('/get_statistics', response_model=list[schemas.Statistic])
def get_statistics(skip: int = 0, limit: int = 200, db: Session = Depends(get_db)):
    items = Operations.get_statistics(db, skip=skip, limit=limit)
    return items