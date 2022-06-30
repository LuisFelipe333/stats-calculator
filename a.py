import string
from matplotlib.pyplot import title
from fastapi import FastAPI

from modelChar import CharRequestModel

app= FastAPI(title="Statistics calculator",
             description= "Calculate the stats of the characters based on their weapon and artifacts",
             version="1.0.0")

@app.get('/')
def index():
    return "a"

@app.post('/char')
def calculate_char(char: CharRequestModel):
    
    return char.name

def calculate_stats(char: CharRequestModel):
    statics_to_add=[20]
    finish_statics=[16]
    
    
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
    
    hp=hp*(statics_to_add[2])
    hp=hp+statics_to_add[1]
    
    atk=atk*(statics_to_add[4])
    atk=atk+statics_to_add[3]
    
    defense=defense*(statics_to_add[6])
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