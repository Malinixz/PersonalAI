from Exercises.AbdominalRowerExercise import AbdominalRowerExercise
from Exercises.PlankExercise import PlankExercise

class ExerciseFactory:
    @staticmethod
    def create_exercise(exercise_type):
        if exercise_type.lower() == "plank":
            return PlankExercise()
        elif exercise_type.lower() == "abdominal_rower":
            return AbdominalRowerExercise()
        else:
            raise ValueError(f"Exercício não suportado: {exercise_type}")