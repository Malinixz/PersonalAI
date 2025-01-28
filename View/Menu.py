from Factories.ExerciseFactory import ExerciseFactory

def show_exercise_menu():
    """
    Exibe o menu de exercícios com base nos exercícios suportados pela fábrica.
    """
    exercises = ExerciseFactory.get_supported_exercises()
    
    print("Escolha sua opção:\n")
    for key, name in exercises:
        print(f"{key}- {name}")
    print("0 - Sair")
    
    choice = input("Digite o número correspondente à sua escolha: ").strip()
    return choice
