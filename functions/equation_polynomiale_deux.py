import math

from colorama import Fore as F


def equation_polynomiale_deux(a: float, b: float, c: float)->str:
  # Rôle: Renvoyer un message avec les racines éventuelles d'une équation polynomiale de degré au plus 2.
  # Arguments:
  #   a, b et c : réels
  # Variables locales:
  #   delta, solution, first_solution, second_solution : réels
  #   answer : chaine
  # Type retourné: chaine

  delta = (b**2) - (4*a*c)

  if delta < 0:
    answer = f"n'y a {F.RED}aucune solution{F.RESET}."
  else:
    if delta == 0:
      solution = -b / (2*a)
      answer = f"y a {F.GREEN}une solution unique{F.RESET} : {F.GREEN}{str(solution)}{F.RESET}"
    else:
      first_solution = (-b - math.sqrt(delta))/(2*a)
      second_solution = (-b + math.sqrt(delta))/(2*a)
      answer = f"y a {F.GREEN}deux solutions{F.RESET} : {F.GREEN}{str(first_solution)}{F.RESET} et {F.GREEN}{str(second_solution)}{F.RESET}"
  
  return f"{F.CYAN}Delta{F.RESET} vaut {F.CYAN}{str(delta)}{F.RESET}, donc il {answer}"
