from cuvant_din_db_criptat import *
from typing import Optional,Tuple,List,Union
cuvant_criptat=["*","*","R","*"]
cuvant_real="MERE"
class HangmanGame:
    def __init__(self,cuvant_criptat:List[str] | None,cuvant_real:str | None):
        self.cuvant_criptat=cuvant_criptat
        self.cuvant_real=cuvant_real
        self.state_joc()
    def state_joc(self,Win:bool=False)-> Union[str,bool]:
        if "*" not in self.cuvant_criptat:
            return self.cuvant_criptat,True
        return self.cuvant_criptat
    def alege_litera_jucator(self)-> str | None:
        litera_jucator=input("Te rog jucatorule alege litera:")
        return litera_jucator
    def game_state(self)-> bool:
        litere_incercate=[]
        if self.alege_litera_jucator() in self.cuvant_real and self.alege_litera_jucator() not in litere_incercate:
            for i,char in enumerate(self.cuvant_real):
                cuvant_criptat[i]=char
                litere_incercate.append(char)
                
            
        pass
        
        
   
game=HangmanGame(cuvant_criptat,cuvant_real)
        
    

