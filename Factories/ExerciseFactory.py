from Exercises.AbdominalRowerExercise import AbdominalRowerExercise
from Exercises.PlankExercise import PlankExercise
from Exercises.PushUpExercise import PushUpExercise

class ExerciseFactory:
    _exercise_classes = {
        "1": PushUpExercise,
        "2": AbdominalRowerExercise,
        "3": PlankExercise,
    }

    @staticmethod
    def create_exercise(exercise_type):
        """
        Cria uma instância do exercício com base no número escolhido.
        """
        exercise_class = ExerciseFactory._exercise_classes.get(exercise_type)
        if exercise_class:
            return exercise_class()
        else:
            raise ValueError(f"Exercício não suportado")

    @staticmethod
    def get_supported_exercises():
        """
        Retorna uma lista de tuplas contendo os números e nomes dos exercícios suportados.
        """
        return [
            ("1", "Flexão de Braços"),
            ("2", "Abdominal Remador"),
            ("3", "Abdominal Prancha"),
        ]