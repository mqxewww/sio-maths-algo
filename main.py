import re
import traceback

from colorama import Fore as F
from inquirer import Text, prompt

from functions.deviner_nombre import deviner_nombre
from functions.equation_polynomiale_deux import equation_polynomiale_deux
from functions.lancers_de_des import lancers_de_des
from functions.prediction_survie import prediction_survie
from functions.table_multiplication import table_multiplication
from functions.tableau_moyenne import tableau_moyenne
from functions.verif_horaire import verif_horaire

try:
  answer = prompt([
    Text(
      "choice",
      message=f"Entrez le {F.CYAN}code{F.RESET} de l'exercice {F.YELLOW}(voir le fichier README.md){F.RESET}",
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
        print(f"L'{F.CYAN}horaire{F.RESET} rentrée est {F.GREEN}correcte{F.RESET}.")
      else:
        print(f"L'{F.CYAN}horaire{F.RESET} rentrée est {F.RED}incorrecte{F.RESET}.")
    case "3":
      value = prompt([
        Text("nombre", message="Table des",  validate=lambda _, x: re.match("^[1-9]\d*$", x))
      ])
      table_multiplication(int(value["nombre"]))
    case "4":
      print(f"La {F.CYAN}moyenne{F.RESET} des notes entrées est : {F.YELLOW}{tableau_moyenne()}{F.RESET}")
    case "5":
      value = prompt([
        Text("rolls", message="Nombre de lancers",  validate=lambda _, x: re.match("^[1-9]\d*$", x))
      ])
      lancers_de_des(int(value["rolls"]))
    case "6":
      deviner_nombre()
    case _:
      print(f"{F.RED}Code invalide.{F.RESET}")
except Exception:
  print(f"{F.RED}Une erreur est survenue. Erreur:{F.RESET}")
  traceback.print_exc()
