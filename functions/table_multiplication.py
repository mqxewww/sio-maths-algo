from colorama import Fore as F


def table_multiplication(nombre: int)->None:
  # Rôle: Afficher la table de multiplication d'un nombre.
  # Arguments:
  #   nombre: entier
  
  print(f"{F.CYAN}Table{F.RESET} des {F.YELLOW}{nombre}{F.RESET} :")
  for i in range(1, 11):
    print(f"{nombre} x {i} = {F.YELLOW}{nombre * i}{F.RESET}")
