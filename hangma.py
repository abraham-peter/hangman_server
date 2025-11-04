print("Bine ai venit in jocul hangman")
cuvant_cr_str="**R*"
cuvant_cr=list(cuvant_cr_str)
cuvant_de_gasit="MERE"
chances=6
win=False
litere_incercate=[]
print(cuvant_cr)
while(chances>0 or win==False):
    litera_aleasa=input("Te rog ghiceste o litera,jucatorule:")
    if litera_aleasa in cuvant_de_gasit and litera_aleasa not in litere_incercate:
        for i,char in enumerate(cuvant_de_gasit):
                if char==litera_aleasa:
                    cuvant_cr[i]=char
                    litere_incercate.append(char)
        print(cuvant_cr)
    elif litera_aleasa in litere_incercate:
            print(f"Litera este deja in cuvant,ne pare rau mai ai {chances} vieti ramase")
            chances-=1
    else:
        chances-=1
        print(f"Litera incercata nu a fost gasita in cuvant,ai {chances} vieti ramase")
        litere_incercate.append(litera_aleasa)
        if "*" not in cuvant_cr:
            win=True
            