# ceci est un dictionnaire
recette = {
  "nom": "tarte au pomme",
  "temps": 30,
  "ingredients": ["pomme", "farine", "sucre", "huile", "caramel"],
  "etape": {
    "preparation": ["couper des pommes", "preparer les feuilles à cuisine", "....."],
    "cuissson": ["cuire au four à 250° pendant 30mn"]
  }
}

print(recette)


# comment acceder au valeur et les modifier
print(recette["nom"])

recette["nom"] = "j'ai changé de nom"
print(recette["nom"])

print("-" * 40)

# ajouter un element à la fin
recette["niveau"] = "debutant"
print(recette)

print("-" * 40)

# mettre à jour le tableau
recette.update({
  "nom": "j'ai encore rechangé le nom",
  "type": "dessert"
})
print(recette)
print("-" * 40)

# effacer la clé temps
del recette["temps"]

print(recette)
print("-" * 40)

# effacer un element et le mettre dans une variable et l'afficher
niveau = recette.pop("niveau")

print(f"l'element effacé est {niveau}")
print(f"voici le nouveau tableau - {recette}")
print("-" * 40)

# boucler dans un dictionnaire - afficher les clés
for cle in recette:
  print(f"la clé - {cle}")

print("-" * 40)

  
# boucler et afficher les clés et valeurs
for cle, valeur in recette.items():
  print(f"la clé est {cle} et la valeur est {valeur}")

# la fonction get
print(recette("origine", "italie"))
