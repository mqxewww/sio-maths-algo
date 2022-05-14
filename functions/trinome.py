import math

from colorama import Fore


def trinome(a: float, b: float, c: float)->str:
  # Rôle: Renvoyer un message avec les racines éventuelles d'un trinôme du second degré
  # Arguments:
  #   a, b et c : réels
  # Variables locales:
  #   delta, solution, firstSolution, secondSolution : réels
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
      firstSolution = (-b - math.sqrt(delta))/(2*a)
      secondSolution = (-b + math.sqrt(delta))/(2*a)
      answer = f"y a {Fore.GREEN}deux solutions{Fore.RESET} : {Fore.GREEN}{str(firstSolution)}{Fore.RESET} et {Fore.GREEN}{str(secondSolution)}{Fore.RESET}"
  
  return f"{Fore.CYAN}Delta{Fore.RESET} vaut {Fore.CYAN}{str(delta)}{Fore.RESET}, donc il {answer}"
