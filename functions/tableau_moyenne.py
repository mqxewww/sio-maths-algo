import re

from inquirer import Text, prompt


def tableau_moyenne()-> float:
  # Rôle: Renvoyer la moyenne de 5 notes dans un tableau.
  # Variables locales:
  #   noteList: tableau
  #   totalNotes: réel
  # Type retourné: réel
  
  noteList = []
  totalNotes = 0

  for pos in range(0, 5):
    answer = prompt([
      Text(
        "choice",
        message=f"Choisissez le nombre réel n°{pos + 1}",
        validate= lambda _, x: re.match("(\d+(?:\.\d+)?)", x)
      )
    ])
    noteList.append(float(answer["choice"]))

  for note in noteList:
    totalNotes += note

  return totalNotes / len(noteList)
