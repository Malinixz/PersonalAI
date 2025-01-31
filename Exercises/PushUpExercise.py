from Exercises.IExercise import Exercise
from Strategies.PushUpCheckStrategy import PushUpPositionCheckStrategy


class PushUpExercise(Exercise):
    def __init__(self):
        super().__init__(PushUpPositionCheckStrategy())
        self.calories = 0.6

    def get_exercise_name(self):
        return "Flexao de Braco"

    def get_calories(self, elapsed_time):
        return self.calories * self.repetitions