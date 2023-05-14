import random

juste_prix = random.randint(0, 1000)
estimation = -1
abandon = False

print("deviner le juste prix ")
print("-----------------------")

while estimation != juste_prix:
  
  instruction = input("quel est ton estimation [q: quitter!] ")
  if not instruction.isnumeric():
    if instruction == "q":
      abandon = True
      break
    else:
      print("entrez un nombre ou q pour quitter")
      continue
  
  estimation = int(instruction)
    
  if estimation < juste_prix:
    print("c'est plus")
  
  if estimation > juste_prix:
    print("c'est moins")

if abandon:
  print(f"dommage, le prix était {juste_prix} €")  
print(f"tu as bien trouvé le prix - {juste_prix} €")  
