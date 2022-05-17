from colorama import Fore


def table_multiplication(nombre: int)->None:
  # Rôle: Afficher la table de multiplication d'un nombre.
  # Arguments:
  #   nombre: entier
  
  print(f"{Fore.CYAN}Table{Fore.RESET} des {Fore.YELLOW}{nombre}{Fore.RESET} :")
  for i in range(1, 11):
    print(f"{nombre} x {i} = {Fore.YELLOW}{nombre * i}{Fore.RESET}")
