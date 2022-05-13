import inquirer

questions = [
  inquirer.List(
    "size",
    message="Sélectionnez le calcul à effectuer",
    choices=["Trinome du second degré", "autre"]
  )
]

answer = inquirer.prompt(questions)
match answer:
  case "Trinome du second degré":
    print(1)
  case _:
    print(0)
