# A F I C C H
# 1 1 2 2 2 2
# 0 0 1 2 3 3
# A A A = K K

# AAA=KK

assasins = input();
kamikase = input();
armas = input();
puntos_assasins = 0;
puntos_kamikase = 0;

for arma in armas:    

    if (arma in assasins):
        puntos_assasins += 1;
    
    if (arma in kamikase):
        puntos_kamikase += 1;

    if(puntos_assasins > puntos_kamikase):
        print("A", end="");
    elif(puntos_kamikase > puntos_assasins):
        print("K", end="");
    else:
        print("=",end="")


        
    
