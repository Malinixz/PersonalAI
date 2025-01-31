from Strategies.PositionCheckStrategy import PositionCheckStrategy
from Utils import Utils


class PushUpPositionCheckStrategy(PositionCheckStrategy):
    def __init__(self):
        self.repetitions = 0
        self.last_position = False
        self.is_valid_cycle = False

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val

    def check_position(self, landmarks):
        try:
            left_elbow_angle = Utils.find_angle(landmarks.landmark, 11, 13, 15)
            right_elbow_angle = Utils.find_angle(landmarks.landmark, 12, 14, 16)
            left_body_alignment = Utils.find_angle(landmarks.landmark, 11, 23, 25)
            right_body_alignment = Utils.find_angle(landmarks.landmark, 12, 24, 26)

            # Lógica da posição baixa
            position_down = (
                self.is_within_range(left_elbow_angle, 50, 90) and
                self.is_within_range(right_elbow_angle, 50, 90)
            )

            # Lógica da posição alta
            position_up = (
                self.is_within_range(left_elbow_angle, 120, 180) and
                self.is_within_range(right_elbow_angle, 120, 180) and
                self.is_within_range(left_body_alignment, 155, 190) and
                self.is_within_range(right_body_alignment, 155, 190)
            )

            # Contagem de repetições
            if position_down and not self.last_position:
                self.last_position = True
                self.is_valid_cycle = True
            elif position_up and self.last_position and self.is_valid_cycle:
                self.repetitions += 1
                self.last_position = False
                self.is_valid_cycle = False

            # Feedback para a tela
            if position_up:
                return True, f"Repeticoes: {self.repetitions}"
            elif position_down:
                return False, f"Repeticoes: {self.repetitions}"
            else:
                return False, f"Repeticoes: {self.repetitions}"

        except Exception as e:
            return False, f"Erro ao calcular ângulos: {str(e)}"