from Exercises.IExercise import Exercise
from Strategies.PlankCheckStrategy import PlankPositionCheckStrategy


class PlankExercise(Exercise):
    def __init__(self):
        super().__init__(PlankPositionCheckStrategy())
        self.calories = 0.2

    def get_exercise_name(self):
        return "Prancha Abdominal"

    def get_calories(self, elapsed_time):
        return self.calories * elapsed_time