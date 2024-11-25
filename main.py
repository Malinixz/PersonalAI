from Core.ExerciseManager import ExerciseManager

def main():
    

    print("Escolha sua opção:\n")
    print("1- Abdominal Remador")
    print("2- Flexão de Braços")
    print("3- Abdominal Prancha")
    print("4- Sair")
    choice = input("Digite o número correspondente à sua escolha: ").strip()

    if choice == "4":
        print("Saindo...")
        return

    exercise_type_map = {
        "1": "abdominal_rower",
        "2": "push-up",
        "3": "plank"
    }

    exercise_type = exercise_type_map.get(choice)
    if not exercise_type:
        print("Erro: Escolha inválida. Por favor, escolha uma opção válida.")
        return


    video_path = input("Digite o caminho do vídeo (deixe vazio para usar a webcam): ").strip()
    use_camera = video_path == ""

    # Escolha de modos apenas se a câmera for usada
    if use_camera:
        print("\nEscolha o modo:")
        print("1- Por tempo (máximo de repetições em 30s)")
        print("2- Por repetições (X repetições no menor tempo possível)")
        mode_choice = input("Digite o número correspondente ao modo: ").strip()

        if mode_choice == "1":
            mode = "time"
        elif mode_choice == "2":
            mode = "repetitions"
        else:
            print("Erro: Modo inválido. Por favor, escolha uma opção válida.")
            return

        if mode == "repetitions":
            total_repetitions = int(input("Digite o número de repetições que deseja completar: ").strip())
        else:
            total_repetitions = None
    else:
        # Se não for câmera, usamos um modo padrão (vídeo sem tempo/repetições)
        mode = "default"
        total_repetitions = None

    video_path = 0 if use_camera else video_path

    exercise_manager = ExerciseManager(exercise_type, video_path, mode, total_repetitions)
    try:
        exercise_manager.run()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()