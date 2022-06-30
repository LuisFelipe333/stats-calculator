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
    atk_base=char.base_atk+char.weapon_atk_base
    
    
    
    
    
    
    return char.name

# flat_atk: 1
# per_atk: 2
# flat_def: 3
# per_def
# elemental mastery: int
# ctr: int
# ctd: int
# healing_bonus:int
# energy_recharge:int
# pyro_dmg:int
# hydro_dmg:int
# electro_dmg:int
# anemo_dmg:int
# cryo_dmg:int
# geo_dmg:int
# dendro_dmg:int
# phys_dmg:int