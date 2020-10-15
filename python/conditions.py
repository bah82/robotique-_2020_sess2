# les ondition permettent de verifier une comparaison 
# le resultat d'une compariaison est soit  vrai.. soit faut
# si le resultat est vrai alors, on excute la condition
# il existe 3 condition possible:
# if = si 
# elif = sinon si ...
# else = sinon (par defaut)
# 
# les different oprateurs comparaison sont :
# > strictement plus grand 
# > strictement plus petit
# == egale 
# >= plus grand ou egale 
# <= plus petit egale
# != different, pas egale
#  

chiffre = 14

if chiffre % 2 == 0: # si le reste de la division est egale a 0
  print("chiffre pair")
else:
  print("chiffre impair")

if chiffre >10:
  print("plus grand que 10")
elif chiffre < 10 :
  print ("plus petit que 10")      
elif chiffre == 10 :
  print ("est égale a 10")  

text = "maison"
lettre ="e"

if lettre in text:
  print(lettre,"est dans",text)
else:
  print(lettre,"nest pas dans",text)  