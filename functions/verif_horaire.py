def verif_horaire(schedule: str)->bool:
  # Rôle: Renvoyer si oui ou non l'horaire entrée est correcte.
  # Arguments:
  #   schedule: chaine
  # Variables locales:
  #   str_list: liste de chaines
  #   a, b, c: entier
  #   d: chaine
  # Type retourné: booléen

  str_list = []

  for (pos, char) in enumerate(schedule):
    str_list.append(char)
  
  try:
    a = int(str_list[0])
    b = int(str_list[1])
    d: str = str_list[2]
    c = int(str_list[3])
    int(str_list[4])
  except Exception:
    return 0
  
  if a <= 2 and not (b >= 4 and a == 2) and c <= 5 and d == ":":
    return 1
  else:
    return 0
