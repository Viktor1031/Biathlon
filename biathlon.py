import random
game_is_on=True


alla_skyttar=[]

class skytt:
    def __init__(self,namn,skill,trötthet):
        self.namn=namn
        self.skill=skill
        self.trötthet=trötthet
        self.måltavla=[0,0,0,0,0] 

def skapa_skytt(spelare):
    alla_skyttar.append(spelare)

def skriv_ut_skytt_lista(skytt_array):
    for x in range(len(skytt_array)):
         print(str(x+1)+". "+skytt_array[x].namn)
         
skapa_skytt(skytt("Hanna Öberg", 80, 20))
skapa_skytt(skytt("Sara Andersson", 75, 5))
skapa_skytt(skytt("Sara Sjöström", 5, 90))
skapa_skytt(skytt("Måns", random.randint(0,100), 20)) #Eftersom vi aldrig testat skidskytte vet vi inte hur bra vi är
skapa_skytt(skytt("Viktor", random.randint(0,100), 50)) #Så en skill mellan 0-100 är korrekt. 


def måltavla_klar(måltavla_array):
    for x in måltavla_array:
        if x==0:
            return False
    return True
    

def rita_måltavla(måltavla_array):
    måltavla_string=""
    for x in måltavla_array:
        if x==0: #Alltså att pricken är noll
            måltavla_string+="*"
        elif x==1:
            måltavla_string+="o"
    print(måltavla_string)
    
def skjut(skytt, prick):
        print(skytt.namn + " skjuter!")
        if skytt.skill>=random.randint(0,100):
            if skytt.trötthet<=random.randint(0,100):
                skytt.måltavla[prick]=1
                print("Fullträff!")
            else:
                print("Zzz....")
        else:
            print("skill issue")
        print()


nuvarande_spelare_index=0
spelare_med_i_spelet=[]
game_state=0

while game_is_on:
    if game_state==0:
        print("Välj vilka spelare som ska vara med genom att skriva in nummret. Eller skriv start för att börja.")
        
        skriv_ut_skytt_lista(alla_skyttar)
            
        player_selection=input()
        
        try:
            if player_selection=="start":
                game_state=1
            spelare_med_i_spelet.append(alla_skyttar[int(player_selection)-1])

            
        except:
            print("Du måste inputa ett nummer mellan 1-5")
            
    elif game_state==1:
        
        spelare=spelare_med_i_spelet[nuvarande_spelare_index]
        print("Välj ett nummer mellan 1-5 som " + spelare.namn + " ska skjuta på")
        rita_måltavla(spelare.måltavla)
    
        player_selection=input()
        
        
        try:
            skjut(spelare,int(player_selection)-1)
            print(spelare.namn+ "s nuvarande tavla: ")
            rita_måltavla(spelare.måltavla)
            print("He")
            if måltavla_klar(spelare.måltavla)==True:
                print()
                print(spelare.namn+" Vann!! ")
                print()
                game_is_on=False
            else:
                nuvarande_spelare_index+=1
                if nuvarande_spelare_index>=len(spelare_med_i_spelet):
                    nuvarande_spelare_index=0
        except:
            print("Du måste inputa ett nummer mellan 1-5")
    
        
    