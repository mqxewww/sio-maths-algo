import random

from colorama import Fore as F


def lancers_de_des(rolls: int)->None:
  # Rôle: Afficher un graphique qui représente x lancers aléatoires de dés.
  # Arguments:
  #   rolls: entier
  # Variables locales:
  #   results_list: tableau
  #   amount: entier
  #   percentage: réel

  results_list = [""] * rolls

  for pos in range(0, rolls):
    results_list[pos] = random.randint(1, 6)

  print(f"{F.CYAN}Représentation{F.RESET} des {F.YELLOW}chiffres{F.RESET} obtenus :")

  for pos in range(1, 7):
    amount = results_list.count(pos)
    percentage = (amount / len(results_list)) * 100
    print(f"{F.YELLOW}{pos}{F.RESET} : {'=' * round(percentage)} • {amount}/{len(results_list)} ({F.YELLOW}{round(percentage, 2)}%{F.RESET})")
