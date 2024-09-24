def get_flippblipp(n):
    
    if n%15==0:
        return "flippblipp"
    elif n%3==0:
        return "flipp"
    elif n%5==0:
        return "blipp"
    
    return str(n)

n=1
has_not_lost=True

while has_not_lost:
    print("Förra: "+get_flippblipp(n))
    print("Nuvarande nummer: "+str(n+1))
    print("Vad är nummret? blipp, flipp, flippblipp eller nummret")
    player_input=input()
    
    if player_input==get_flippblipp(n+1):
        n+=1
        print("Rätt!! \n")
        continue;
    
    print("Fel")
    print("Rätt svar var: "+ get_flippblipp(n+1))
    print("Game over! \n")
    
    has_not_lost=False
    
    
    
        
    
    
    
    
    