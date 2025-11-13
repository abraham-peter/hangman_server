from cuvant_din_db_criptat import *
from typing import Optional,Tuple,List,Union,NoReturn
cuvant_criptat=["*","*","R","*"]
cuvant_real="MERE"
class GameState:
    def __init__(self,pattern,cuvant)-> NoReturn:
        super().__init__()
        self.pattern=pattern
        self.cuvant=cuvant
        self.chances=6
        self.litere_incercate=[]
        self.vizualizare_pattern(None)
        self.victory_state(None)
    def vizualizare_pattern(self,litera_user)-> bool | None: 
        print(self.pattern)
        if litera_user not in self.litere_incercate and litera_user in self.cuvant:
            for i,char in enumerate(self.cuvant):
                if char==litera_user:
                    self.pattern[i]=char
            self.litere_incercate.append(char)
            print(self.pattern)
            return True
        return False
                        
    def victory_state(self)-> bool | None:
        if "*" not in self.pattern:
            return True
        return False
class Exceptii(Exception):
    pass
class PlayerInput:
    def __init__(self,litera_jucator:str | None)-> NoReturn:
        super().__init__()
        self.litera_jucator=litera_jucator
    
    def validari(self)-> NoReturn:
        if len(self.litera_jucator)>1:
            raise Exceptii(f"Imi pare rau ati introdus mai mult de un character,in acest caz lungimea este de{len(self.litera_jucator)} charactere,inceaca din nou si nu introduce mai multe litere.")
        elif len(self.litera_jucator)==0 or self.litera_jucator==None:
            raise Exceptii("Imi pare rau dar nu ai introdus nimic,asa ca incearca din nou.")
        elif self.litera_jucator is not None and not isinstance(self.litera_jucator,str):
            raise Exceptii("Charcterul pe care l-ati ales nu e string,incercati din nou.")
        elif self.litera_jucator is not None and self.litera_jucator is not self.litera_jucator.isalpha():
            raise Exceptii("Din pacate nu ai introdus o litera,doar un character,asa ca te rog sa incerci din nou.")
class JocHangman(PlayerInput,GameState):
    def __init__(self):
        super().__init__()
    def joc_hangman(self):
        while self.chances>0 and not self.wictory_state(None):
            litera_jucator=input("Alege o litera: ")
            try:
                PlayerInput(litera_jucator).validari()
                if self.vizualizare_pattern(litera_jucator) != True:
                    self.chances-=1
                    print(f"Ne pare rau,litera nu se afla in cuvant, {self.chances} sanse ramase.")
                    
            except:
                raise Exceptii("A aparut o eroare,incearca din nou")
         
        
        
        
            
                
                    