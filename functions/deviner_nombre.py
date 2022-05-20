import random
import re

from colorama import Fore as F
from inquirer import Text, prompt


def deviner_nombre()->None:
  # Rôle: Deviner un nombre entre 1 et 500.
  # Variables locales:
  #   random_number, attemps: entier
  #   found: booléen

  random_number = random.randint(1, 500)
  attemps = 0
  found = 0

  while found == 0:
    attemps += 1
    value = prompt([
      Text(
        "number", message=f"Essai n°{F.YELLOW}{attemps}{F.RESET}, entrer un {F.CYAN}nombre{F.RESET} (1 - 500)",
        validate=lambda _,
        x: re.match("^[1-9]\d*$", x)
      )
    ])

    if int(value["number"]) < random_number:
      print(f"Le {F.CYAN}nombre{F.RESET} est plus {F.GREEN}grand{F.RESET} !")
    elif int(value["number"]) > random_number:
      print(f"Le nombre est plus {F.RED}petit{F.RESET} !")
    elif int(value["number"]) == random_number:
      print(f"Le nombre est bien {F.YELLOW}{random_number}{F.RESET} ! Trouvé en {F.CYAN}{attemps} essais{F.RESET}.")
      found = 1
