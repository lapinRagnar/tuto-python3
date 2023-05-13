def dire_bonjour():
  print('hello world')
  print('bonjour')

dire_bonjour()

# fonction avec parametres et parametre par defaut
def temps_de_trajet(distance_en_km, vitesse_en_km_h, nombre_pauses=0, nombre_passagers=0):
  
  temps = distance_en_km / vitesse_en_km_h
  
  temps_de_pauses = nombre_pauses * 5 / 60
  temps_de_pause_passagers = nombre_pauses * nombre_passagers * 2 / 60
  
  total_temps_trajet = temps + temps_de_pauses + temps_de_pause_passagers
  
  return temps, total_temps_trajet

temps_de_trajet(120, 30)

print("-" * 40)

temps_1 = temps_de_trajet(150, 20)
temps_2 = temps_de_trajet(50, 3)

temps_total = temps_1 + temps_2

print(f"le temps total = {temps_1} h + {temps_2} h = {temps_total} h")

print("-" * 40)
# comment utiliser les parametres nommés
temps_3 = temps_de_trajet(distance_en_km=50, vitesse_en_km_h=5, nombre_pauses=5, nombre_passagers=10)
print(f"le temps de trajet est de = {temps_3}")



