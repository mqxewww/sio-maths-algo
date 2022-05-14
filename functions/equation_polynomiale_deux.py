import math

from colorama import Fore


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
    answer = f"n'y a {Fore.RED}aucune solution{Fore.RESET}."
  else:
    if delta == 0:
      solution = -b / (2*a)
      answer = f"y a {Fore.GREEN}une solution unique{Fore.RESET} : {Fore.GREEN}{str(solution)}{Fore.RESET}"
    else:
      first_solution = (-b - math.sqrt(delta))/(2*a)
      second_solution = (-b + math.sqrt(delta))/(2*a)
      answer = f"y a {Fore.GREEN}deux solutions{Fore.RESET} : {Fore.GREEN}{str(first_solution)}{Fore.RESET} et {Fore.GREEN}{str(second_solution)}{Fore.RESET}"
  
  return f"{Fore.CYAN}Delta{Fore.RESET} vaut {Fore.CYAN}{str(delta)}{Fore.RESET}, donc il {answer}"
