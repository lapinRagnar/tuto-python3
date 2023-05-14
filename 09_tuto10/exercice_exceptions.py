nom_fichier = input("quel fichier souhaitez-vous lire?")


try:
  nombre = int(input("combien de fois doit-on imprimer le fichier?"))
  print(f"le fichier {nom_fichier} va etre imprimer {nombre} de fois...")
  with open(nom_fichier) as fp:
    lines = fp.readlines()
    for n in range(nombre):
      for line in lines:
        print(line.strip())
except ValueError:
  print("desolé, tu dois enter un nombre!")
except FileNotFoundError:
  print("desolé, le fichier n'existe pas!")
except Exception:
  print("erreur inatendu!")
else:
  print("tout s'est bien passé!")
finally:
  print("peu importe on affiche ce message, aie aieuuuuuh!")

print("merci d'avoir utilisé notre programme!")

