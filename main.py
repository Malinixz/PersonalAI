from Core.ExerciseManager import ExerciseManager

def main():
    exercise_type = input("Escolha o exercício ('plank', 'abdominal_rower', 'push-up'): ").strip().lower()
    if exercise_type not in ["plank", "abdominal_rower","push-up"]:
        print("Erro: Exercício não suportado. Escolha entre 'plank' ou 'abdominal_rower'.")
        return

    video_path = input("Digite o caminho do vídeo (deixe vazio para usar a webcam): ").strip()
    video_path = 0 if video_path == "" else video_path

    exercise_manager = ExerciseManager(exercise_type, video_path)
    try:
        exercise_manager.run()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()