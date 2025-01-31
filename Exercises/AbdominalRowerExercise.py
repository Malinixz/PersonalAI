from Exercises.IExercise import Exercise
from Strategies.AbdominalRowerCheckStrategy import AbdominalRowerPositionCheckStrategy


class AbdominalRowerExercise(Exercise):
    def __init__(self):
        super().__init__(AbdominalRowerPositionCheckStrategy())
        self.calories = 0.4

    def get_exercise_name(self):
        return "Abdominal Remador"

    def get_calories(self, elapsed_time):
        return self.calories * self.repetitions