# Sistema de Análise de Postura para Exercícios
#
# Integrantes:
#   João Victor Ferrareis Ribeiro
#   Mateus Lannes Cunha
#   Miguel Malini Louvem
#   Perseu Fernandes Machado de Oliveira
#

from Core.ExerciseManager import ExerciseManager
from Core.VideoProcessor import VideoProcessor
from Factories.ExerciseFactory import ExerciseFactory
from View.Menu import show_exercise_menu

def main():
    

    choice = show_exercise_menu()
        
    # Verificar se o usuário escolheu "Sair"
    if choice == "0":
        print("Saindo...")
        return

    video_path = input("Digite o caminho do vídeo (deixe vazio para usar a webcam): ").strip()
    use_camera = video_path == ""

    # Escolha de modos apenas se a câmera for usada
    if use_camera:
        if choice == "3":
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
                print("Erro: Modo inválido. Por favor, escolha uma opção válida.")
                return
    else:
        # Se não for câmera, usamos um modo padrão (vídeo sem tempo/repetições)
        mode = "default"
        total_repetitions = None
        max_duration = None

    video_path = 0 if use_camera else video_path

    # exercise_manager = ExerciseManager(choice, video_path, mode, total_repetitions, max_duration)
    
    exercise = ExerciseFactory.create_exercise(choice)
    exercise_manager = ExerciseManager(exercise, video_path, mode, total_repetitions, max_duration)
    try:
        exercise_manager.run()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()