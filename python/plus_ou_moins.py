# on importe une librairie pour choisir un nombre aleatoire
import random

# on cree une variable nombre cavhe
# on y stock un nombre aleatoire entre 0 et 100
# on fait appel a la fonction randint qui se trouve dans random



nombre_cache = random.randint(0,100)

print("tape un nombre entre 0 et 100")
entrer_joueur = int( input (">>")) 
if entrer_joueur < nombre_cache:
    print(ton nombre est plus petite)
    
elif entrer_joueur > nombre_cache:
    print(ton nombre est plus grand)
else:
    print("bravo")    


