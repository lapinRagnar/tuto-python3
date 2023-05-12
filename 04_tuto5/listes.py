liste_vide = []
liste_element_meme_type = [54, 1545, 1111, 2545, 2222]
liste_heterogene = [5422, True, 22.45, "bonjour", [3323, 444]]

# les opérations

print(f"la liste heterogene = {liste_heterogene}")
print("#####################################################################")

print(liste_heterogene[2])
print(liste_heterogene[4][1])

liste_heterogene[2] = 100000
print(liste_heterogene)

liste_heterogene.append(666)
print(liste_heterogene)

# on ajoute à l'index 3
liste_heterogene.insert(3, 777777)
print(liste_heterogene)

# on supprime l'element à l'index 0
del liste_heterogene[0]
print(liste_heterogene)

# on supprime et affice le dernier element
dernier_element = liste_heterogene.pop()
print(liste_heterogene)
print(f"le dernier element qu'on a effacé est {dernier_element}")

# on supprime l'element à index 2
element_a_l_index_2 = liste_heterogene.pop(3)
print(liste_heterogene)
print(f"l'element supprimé à l'index 2 est {element_a_l_index_2}")

print("#####################################################################")

# comment afficher le dernier element de la liste
print(f"dernier element de la liste {liste_heterogene[-1]}")

# afficher la longueur de la liste
print(f"la liste complet : {liste_heterogene}")
print(f"la longeur de la liste est: {len(liste_heterogene)}")

# concatener 2 liste 
somme_des_listes = liste_heterogene + liste_element_meme_type
print(f"la somme des 2 listes = {somme_des_listes}")

# ajouter 2 elements dans la liste
somme_des_listes.extend(["a", 5421411, False])
print(f"ajout avec extend - {somme_des_listes} ")

# le slicing
# afficher les elements de l'index 1 à 4
print(f"les 4 premiers elements : {somme_des_listes[1:5]} ")

# afficher à partir de l'index 5 jusqu'à la fin
print(f"afficher à partir de l'index 5 jusqu'à la fin - {somme_des_listes[5:]}")