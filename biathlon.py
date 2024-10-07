from random import randint
game_is_on=True

alla_skyttar=[] #Det är en array av alla skyttar som går att välja mellan

class skytt: #Definitionen av vad en skytt är
    def __init__(self,namn,skill,trötthet):
        self.namn=namn
        self.skill=skill
        self.trötthet=trötthet
        self.måltavla=[0,0,0,0,0] #0=tom 1=träffad Varje skytt har en egen måltavla

def skapa_skytt(spelare): #Vi har en funktion för att lägga till skyttar till alla skyttar som går att välja bland.
    alla_skyttar.append(spelare)

def skriv_ut_skytt_lista(skytt_array): #Vi går igenom alla skyttar i en array av skyttar och printar deras namn samt index
    for x in range(len(skytt_array)):
         print(str(x+1)+". "+skytt_array[x].namn)
         
skapa_skytt(skytt("Hanna Öberg", 80, 20)) #Vi definerar alla skyttar som kan bli valda ur alla_skyttar
skapa_skytt(skytt("Sara Andersson", 75, 5))
skapa_skytt(skytt("Sara Sjöström", 5, 90))
skapa_skytt(skytt("Måns", randint(0,100), 20)) #Eftersom vi aldrig testat skidskytte vet vi inte hur bra vi är
skapa_skytt(skytt("Viktor", randint(0,100), 50)) #Så en skill mellan 0-100 är korrekt. 


def måltavla_klar(måltavla_array): #Denna funktion kollar om en måltavla_array har 5/5 träffar.  
    for x in måltavla_array:
        if x==0:
            return False
    return True
    

def rita_måltavla(måltavla_array): # Vi ritar en måltavla
    måltavla_string=""
    for x in måltavla_array:
        if x==0: #Alltså att pricken är noll
            måltavla_string+="*"
        elif x==1:
            måltavla_string+="o"
    print(måltavla_string)
    
def skjut(skytt, prick): #Vi skjuter med en skytt på ett index prick.
        print(skytt.namn + " skjuter!")
        if skytt.skill>=randint(0,100):
            if skytt.trötthet<=randint(0,100):
                if skytt.måltavla[prick] == 1:
                    print("Du träffade en prick du redan träffat!")
                else:
                    skytt.måltavla[prick]=1
                    print("Fullträff!")
            else:
                print("Zzz....")
        else:
            print("skill issue")
        print()


nuvarande_spelare_index=0 #När spelet är igång är denna vilken spelare som ska skjuta
spelare_med_i_spelet=[] #Listan av spelare man har valt
game_state=0 

while game_is_on:
    if game_state==0: #Välj vilka spelare som ska vara med
        print("Välj vilka spelare som ska vara med genom att skriva in nummret. Eller skriv start för att börja.")
        
        skriv_ut_skytt_lista(alla_skyttar)
            
        player_selection=input()
        
        try:
            if player_selection=="start":
                game_state=1
            spelare_med_i_spelet.append(alla_skyttar[int(player_selection)-1])

            
        except:
            print("Du måste inputa ett nummer mellan 1-5")
            
    elif game_state==1: #En spelare i taget skjuter med hjälp av input från spelaren
        
        spelare=spelare_med_i_spelet[nuvarande_spelare_index]
        print("Välj ett nummer mellan 1-5 som " + spelare.namn + " ska skjuta på")
        rita_måltavla(spelare.måltavla)
    
        player_selection=input()
        
        
        try:
            skjut(spelare,int(player_selection)-1)
            print(spelare.namn+ "s nuvarande tavla: ")
            rita_måltavla(spelare.måltavla)
        
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
    
        
    