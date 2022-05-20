from colorama import Fore as F


def prediction_survie(gender: bool, age: int, travel_class: int, price: float, booth_number: int)-> str:
  # Rôle: Renvoyer un message indiquant une prédiction de la chance de survie d'un passager du Titanic suite à son naufrage.
  # Arguments:
  #   age, travel_class, booth_number: entiers
  #   gender: booléen
  #   price: réel
  # Variables locales:
  #   verified_criterias: entier
  #   answer: chaine
  # Type retourné: chaine

  verified_criterias = 0

  if gender == 1:
    verified_criterias += 1
  
  if age <= 18 | age >= 60:
    verified_criterias += 1
  
  if travel_class != 3:
    verified_criterias += 1
  
  if price >= 10.35:
    verified_criterias += 1
  
  if booth_number % 2 == 0 & booth_number % 7 == 0:
    verified_criterias += 1

  match verified_criterias:
    case 5:
      answer = "très probable"
    case 3 | 4:
      answer = "probable"
    case 0:
      answer = "quasiment impossible"
    case _:
      answer = "peu probable"
  
  return f"La {F.CYAN}survie{F.RESET} de ce passager est {F.CYAN}{answer}{F.RESET}."
