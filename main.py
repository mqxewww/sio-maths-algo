import re
import traceback

from colorama import Fore
from inquirer import List, Text, prompt

from functions.trinome import trinome

try:
  answer = prompt([
    List(
      "choice",
      message="Sélectionnez le calcul à effectuer",
      choices=["Trinôme du second degré"]
    )
  ])

  match answer["choice"]:
    case "Trinôme du second degré":
      values = prompt([
        Text("a", message="Premier argument réel (a)", validate=lambda _, x: re.match("(\d+(?:\.\d+)?)", x)),
        Text("b", message="Deuxième argument réel (b)", validate=lambda _, x: re.match("(\d+(?:\.\d+)?)", x)),
        Text("c", message="Troisième argument réel (c)", validate=lambda _, x: re.match("(\d+(?:\.\d+)?)", x)),
      ])
      print(trinome(float(values["a"]), float(values["b"]), float(values["c"])))
    case _:
      print(f"{Fore.RED}Erreur dans le choix du calcul à effectuer.{Fore.RESET}")
except Exception:
  print(f"{Fore.RED}Une erreur est survenue lors du calcul. Erreur:{Fore.RESET}")
  traceback.print_exc()
