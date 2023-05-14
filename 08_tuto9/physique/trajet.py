def temps_de_trajet(distance_en_km, vitesse_en_km_h, nombre_pauses=0, nombre_passagers=0):
  
  temps = distance_en_km / vitesse_en_km_h  
  temps_de_pauses = nombre_pauses * 5 / 60
  temps_de_pause_passagers = nombre_pauses * nombre_passagers * 2 / 60  
  
  return temps + temps_de_pauses + temps_de_pause_passagers