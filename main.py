import re
import traceback

from colorama import Fore
from inquirer import Text, prompt

from functions.equation_polynomiale_deux import equation_polynomiale_deux
from functions.prediction_survie import prediction_survie
from functions.table_multiplication import table_multiplication
from functions.verif_horaire import verif_horaire

try:
  answer = prompt([
    Text(
      "choice",
      message=f"Entrez le {Fore.CYAN}code{Fore.RESET} de l'exercice {Fore.YELLOW}(voir le fichier README.md){Fore.RESET}",
      validate= lambda _, x: re.match(r'^([\s\d]+)$', x)
    )
  ])

  match answer["choice"]:
    case "0":
      values = prompt([
        Text("a", message="Premier argument réel (a)", validate=lambda _, x: re.match("(\d+(?:\.\d+)?)", x)),
        Text("b", message="Deuxième argument réel (b)", validate=lambda _, x: re.match("(\d+(?:\.\d+)?)", x)),
        Text("c", message="Troisième argument réel (c)", validate=lambda _, x: re.match("(\d+(?:\.\d+)?)", x))
      ])
      print(equation_polynomiale_deux(float(values["a"]), float(values["b"]), float(values["c"])))
    case "1":
      values = prompt([
        Text("gender", message="Genre du passager (0 pour homme et 1 pour femme)", validate=lambda _, x: re.match("(?i)(0|1)$", x)),
        Text("age", message="Age du passager", validate=lambda _, x: re.match("^[1-9]\d*$", x)),
        Text("travel_class", message="Classe du voyage du passager (1, 2 ou 3)", validate=lambda _, x: re.match("(?i)(1|2|3)$", x)),
        Text("price", message="Prix du ticket du voyage", validate=lambda _, x: re.match("(\d+(?:\.\d+)?)", x)),
        Text("booth_number", message="Numéro de cabine (entier entre 0 et 762)", validate=lambda _, x: re.match("(?i)([0-6]?[0-9][0-9]?|7[0-5][0-9]|76[0-2])$", x))
      ])
      print(prediction_survie(int(values["gender"]), int(values["age"]), int(values["travel_class"]), float(values["price"]), int(values["booth_number"])))
    case "2":
      value = prompt([
        Text("schedule", message="Heure (HH:MM)")
      ])
      if verif_horaire(value["schedule"]):
        print(f"L'{Fore.CYAN}horaire{Fore.RESET} rentrée est {Fore.GREEN}correcte{Fore.RESET}.")
      else:
        print(f"L'{Fore.CYAN}horaire{Fore.RESET} rentrée est {Fore.RED}incorrecte{Fore.RESET}.")
    case "3":
      value = prompt([
        Text("nombre", message="Table des",  validate=lambda _, x: re.match("^[1-9]\d*$", x))
      ])
      table_multiplication(int(value["nombre"]))
    case _:
      print(f"{Fore.RED}Code invalide.{Fore.RESET}")
except Exception:
  print(f"{Fore.RED}Une erreur est survenue. Erreur:{Fore.RESET}")
  traceback.print_exc()
