from cuvant_din_db_criptat import *
from typing import Optional,Tuple,List
class HangmanGame:
    id=0
    def __init__(self,cuvant_criptat_intrare:str,cuvant_de_ghicit_intrare:str):
        self.cuvant_criptat=cuvant_criptat_intrare
        self.cuvant_de_ghicit=cuvant_de_ghicit_intrare
        print(cuvant_criptat_intrare)
        self.hangman_game(self.cuvant_de_ghicit,self.cuvant_criptat,id)
        self.state_joc(self.cuvant_de_ghicit)
    def hangman_game(self,cuvant_de_ghicit:str,cuvant_criptat:str,id:int)->Optional[bool]:
        print("Baga litera,jucatorul cu nuamrul {id}")
        self.litera_utilizator=input()
        lista_cuvant_de_ghicit=list(self.cuvant_de_ghicit)
        if self.litera_utilizator in self.cuvant_de_ghicit:
            print("Bravo ai ghicit litera {self.litera_utilizator} este in cuvant.")
            for char,i in enumerate(self.cuvant_de_ghicit):
                if char==lista_cuvant_de_ghicit:
                    self.cuvant_criptat[i]=char
    def state_joc(self,cuvant_de_ghicit)->Tuple[Optional[str],bool]:
        print("Merge")
        if "*" in self.cuvant_de_ghicit:
            return self.cuvant_de_ghicit,False
            print("*")
        return self.cuvant_de_ghicit,True

print("Bine ai venit la jocul hangman!")
game=HangmanGame(cuvant_criptat_declarat,cuvant_de_ghicit_declarat)

