from bonjour import dire_bonjour, dire_au_revoir
import physique

nom = input("quel est ton nom?")
distance = float(input("quel distance veut-tu parcourir?"))
vitesse_en_ms = float(input("A quelle vitesse? [m/s] "))

# dire bonjour à l'utilisateur
dire_bonjour(nom)

# convertir vitesse en km/h
vitesse_en_kmh = physique.vitesse.convertir_ms_en_kmh(vitesse_en_ms)

# calculer le temps de trajet
temps_de_trajet = physique.trajet.temps_de_trajet(distance_en_km=distance, vitesse_en_km_h=vitesse_en_kmh)

# afficher le temps de tranjet
print(f"votre temps de trajet est de {temps_de_trajet} heures")

# dire au revoir
dire_au_revoir(nom)
