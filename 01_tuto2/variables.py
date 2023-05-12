# les variables de base

premier_nombre = 13
deuxieme_nombre = 32.5

premier_texte = "Hello world"
deuxieme_texte = "lapinRagnar"

premier_booleen = True
deuxieme_booleen = False

print(premier_nombre)
print(type(premier_nombre))

print(deuxieme_nombre)
print(type(deuxieme_nombre))

print(premier_nombre)
print(deuxieme_texte)

print(type(premier_texte), type(deuxieme_texte))

print(premier_booleen)
print(deuxieme_booleen)
print(type(premier_booleen), type(deuxieme_booleen))


# operations
premiere_somme = premier_nombre + deuxieme_nombre + 14
premiere_multiplication = premiere_somme * 2000
print(premiere_somme)
print(premiere_multiplication)

somme_de_texte = premier_texte + " " + deuxieme_texte
print(somme_de_texte)


premier_et_deuxieme_booleen = premier_booleen and deuxieme_booleen
print(premier_et_deuxieme_booleen)

premier_ou_deuxieme_booleen = premier_booleen or deuxieme_booleen
print(premier_ou_deuxieme_booleen)

not_premier_booleen = not premier_booleen # return false

comparaison_de_nombre = premier_nombre < deuxieme_nombre
print(comparaison_de_nombre)

nombre_un_plus_petit_que_deux = premier_nombre < deuxieme_nombre
nombre_un_plus_grand_ou_egal_a_deux = premier_nombre >= deuxieme_nombre
nombre_un_egal_a_deux = premier_nombre == deuxieme_nombre
nombre_un_different_de_nombre_deux = premier_nombre != deuxieme_nombre

print(nombre_un_plus_grand_ou_egal_a_deux, nombre_un_plus_petit_que_deux, nombre_un_egal_a_deux, nombre_un_different_de_nombre_deux)


# les conversions
nombre_decimal = 15.241
print(type(nombre_decimal), nombre_decimal)
print(int(nombre_decimal))

nombre_entier = 25411
print(f"nombre entier {nombre_entier} - convertis en float {float(nombre_entier)}")

nombre_decimal_en_texte = str(nombre_decimal) + " est ton nombre en string!"
print(nombre_decimal_en_texte)

# lire une valeur entrée par l'utilisateur
valeur_utilisateur = input("entrez ton nom?")
print(f"ton nom est {valeur_utilisateur}")