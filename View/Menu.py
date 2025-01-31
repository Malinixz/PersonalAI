from Factories.ExerciseFactory import ExerciseFactory

def show_exercise_menu():
    """
    Exibe o menu de exercícios com base nos exercícios suportados pela fábrica.
    Retorna a escolha do usuário.
    """
    exercises = ExerciseFactory.get_supported_exercises()
    
    print("Escolha sua opção:\n")
    for key, name in exercises:
        print(f"{key}- {name}")
    print("0 - Sair")
    
    choice = input("Digite o número correspondente à sua escolha: ").strip()
    return choice

def get_exercise_mode(choice, use_camera):
    """
    Obtém o modo de execução (tempo, repetições ou padrão) com base na escolha do usuário.
    Retorna o modo, duração máxima e número de repetições.
    """
    if use_camera:
        if choice == "3":  # Prancha Abdominal
            print("\nVocê escolheu 'Abdominal Prancha'. O modo disponível é 'tempo'.")
            mode = "time"
            max_duration = int(input("Digite o tempo desejado para realizar o exercício (em segundos): ").strip())
            total_repetitions = None
        else:
            print("\nEscolha o modo:")
            print("1- Por tempo (máximo de repetições em X segundos)")
            print("2- Por repetições (X repetições no menor tempo possível)")
            mode_choice = input("Digite o número correspondente ao modo: ").strip()

            if mode_choice == "1":
                mode = "time"
                total_repetitions = None
                max_duration = int(input("Digite o tempo desejado para realizar o exercício (em segundos): ").strip())
            elif mode_choice == "2":
                mode = "repetitions"
                total_repetitions = int(input("Digite o número de repetições que deseja completar: ").strip())
                max_duration = None
            else:
                raise ValueError("Erro: Modo inválido. Por favor, escolha uma opção válida.")
    else:
        # Modo padrão para vídeos
        mode = "default"
        total_repetitions = None
        max_duration = None

    return mode, max_duration, total_repetitions