from Strategies.PositionCheckStrategy import PositionCheckStrategy
from Utils import Utils


class AbdominalRowerPositionCheckStrategy(PositionCheckStrategy):
    def __init__(self):
        self.repetitions = 0
        self.excentric = False

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val

    def check_position(self, landmarks):
        try:
            elbow_angle = Utils.find_angle(landmarks.landmark, 12, 14, 16)
            left_elbow_angle = Utils.find_angle(landmarks.landmark, 11, 13, 15)
            hip_angle = Utils.find_angle(landmarks.landmark, 11, 23, 25)
            left_hip_angle = Utils.find_angle(landmarks.landmark, 12, 24, 26)
            knee_angle = Utils.find_angle(landmarks.landmark, 23, 25, 27)
            left_knee_angle = Utils.find_angle(landmarks.landmark, 24, 26, 28)

            # Posição inicial (deitado)
            initial_position = (
                self.is_within_range(elbow_angle, 90, 185) and
                self.is_within_range(left_elbow_angle, 90, 185) and
                self.is_within_range(hip_angle, 140, 185) and
                self.is_within_range(left_hip_angle, 140, 185) and
                self.is_within_range(knee_angle, 140, 185) and
                self.is_within_range(left_knee_angle, 140, 185)
            )

            # Posição final (sentado)
            final_position = (
                self.is_within_range(elbow_angle, 90, 185) and
                self.is_within_range(left_elbow_angle, 90, 185) and
                self.is_within_range(hip_angle, 25, 50) and
                self.is_within_range(left_hip_angle, 25, 50) and
                self.is_within_range(knee_angle, 25, 50) and
                self.is_within_range(left_knee_angle, 20, 50)
            )

            # Lógica de contagem
            if final_position and not self.excentric:
                self.repetitions += 1
                self.excentric = True
            elif initial_position and self.excentric:
                self.excentric = False

            # Feedback para a tela
            if final_position:
                return True, f"Repeticoes: {self.repetitions}"
            else:
                return False, f"Repeticoes: {self.repetitions}"

        except Exception as e:
            return False, f"Erro ao calcular ângulos: {str(e)}"