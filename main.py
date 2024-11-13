from Core.ExerciseManager import ExerciseManager

def main():
    # FALTA A LOGICA PARA INPUT
    exercise_manager = ExerciseManager("plank") # PARAMETROS : (String do exercicio, Caminho do Video) | Caminho Vazio => liga WebCam
    exercise_manager.run()

if __name__ == "__main__":
    main()