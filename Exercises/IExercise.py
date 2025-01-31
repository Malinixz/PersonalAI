from Strategies import PositionCheckStrategy


class Exercise:
    def __init__(self, position_check_strategy: PositionCheckStrategy):
        self.position_check_strategy = position_check_strategy
        self.repetitions = 0

    def check_position(self, landmarks):
        return self.position_check_strategy.check_position(landmarks)

    def get_exercise_name(self):
        raise NotImplementedError

    def get_calories(self, elapsed_time):
        raise NotImplementedError