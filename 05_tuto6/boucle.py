liste_entiers = [5, 7, 8, 55, 12145]

for entier in liste_entiers:
  print(entier)

print("#" * 40)  

for nombre in range(5):
  print(nombre)
  
print("#" * 40)  

# affiche à partir de l'indice 3 jusqu'à 5
for n in range(3, 5):
  print(n)

print("#" * 40)  

# on increment de 5
for n in range(1, 20, 5):
  print(n)

print("#" * 40)  

# on commence par 30 jusqu'à 5 et on decremente de -5
for n in range(30, 3, -5):
  print(n)

print("#" * 40)  

# comment utilisé enumerate
for rep, entier in enumerate(liste_entiers):
  print(f"L'entier {entier} est l'element n° {rep}")
  