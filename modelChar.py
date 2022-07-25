from typing import Optional
from pydantic import BaseModel

class CharRequestModel(BaseModel):
    name:int
    
    
    weapon_id:int
    
    art1_type:Optional[int]=0
    art1_main_stat:Optional[int]=0
    art1_main_stat_value:Optional[float]=0
    art1_stat1:Optional[int]=0
    art1_stat1_value:Optional[float]=0
    art1_stat2:Optional[int]=None
    art1_stat2_value:Optional[float]=0
    art1_stat3:Optional[int]=None
    art1_stat3_value:Optional[float]=0
    art1_stat4:Optional[int]=None
    art1_stat4_value:Optional[float]=0
    
    art2_type:Optional[int]=0
    art2_main_stat:Optional[int]=0
    art2_main_stat_value:Optional[float]=0
    art2_stat1:Optional[int]=0
    art2_stat1_value:Optional[float]=0
    art2_stat2:Optional[int]=None
    art2_stat2_value:Optional[float]=0
    art2_stat3:Optional[int]=None
    art2_stat3_value:Optional[float]=0
    art2_stat4:Optional[int]=None
    art2_stat4_value:Optional[float]=0
    
    art3_type:Optional[int]=0
    art3_main_stat:Optional[int]=0
    art3_main_stat_value:Optional[float]=0
    art3_stat1:Optional[int]=0
    art3_stat1_value:Optional[float]=0
    art3_stat2:Optional[int]=None
    art3_stat2_value:Optional[float]=0
    art3_stat3:Optional[int]=None
    art3_stat3_value:Optional[float]=0
    art3_stat4:Optional[int]=None
    art3_stat4_value:Optional[float]=0
    
    art4_type:Optional[int]=0
    art4_main_stat:Optional[int]=0
    art4_main_stat_value:Optional[float]=0
    art4_stat1:Optional[int]=0
    art4_stat1_value:Optional[float]=0
    art4_stat2:Optional[int]=None
    art4_stat2_value:Optional[float]=0
    art4_stat3:Optional[int]=None
    art4_stat3_value:Optional[float]=0
    art4_stat4:Optional[int]=None
    art4_stat4_value:Optional[float]=0