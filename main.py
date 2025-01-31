# Sistema de Análise de Postura para Exercícios
#
# Integrantes:
#   João Victor Ferrareis Ribeiro
#   Mateus Lannes Cunha
#   Miguel Malini Louvem
#   Perseu Fernandes Machado de Oliveira
#

from Core.ExerciseManager import ExerciseManager
from Factories.ExerciseFactory import ExerciseFactory
from View.Menu import show_exercise_menu, get_exercise_mode  # Funções da View

def main():
    # Exibe o menu de exercícios
    choice = show_exercise_menu()
    
    # Verificar se o usuário escolheu "Sair"
    if choice == "0":
        print("Saindo...")
        return

    # Solicita o caminho do vídeo ou uso da webcam
    video_path = input("Digite o caminho do vídeo (deixe vazio para usar a webcam): ").strip()
    use_camera = video_path == ""

    # Obtém o modo de execução (tempo, repetições ou padrão)
    mode, max_duration, total_repetitions = get_exercise_mode(choice, use_camera)

    # Define o caminho do vídeo (0 para webcam)
    video_path = 0 if use_camera else video_path
    
    # Cria o exercício e o gerenciador
    exercise = ExerciseFactory.create_exercise(choice)
    exercise_manager = ExerciseManager(exercise, video_path, mode, total_repetitions, max_duration)

    # Executa o exercício
    try:
        exercise_manager.run()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()