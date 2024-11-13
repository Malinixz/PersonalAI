from abc import ABC, abstractmethod
import math
import mediapipe as mp

# Classe base abstrata para exercícios
class Exercise(ABC):
    @abstractmethod
    def check_position(self, landmarks):
        pass

    @abstractmethod
    def get_exercise_name(self):
        pass

    # Método find_angle adicionado na classe base
    def find_angle(self, landmarks, p1, p2, p3):
        x1, y1 = (landmarks[p1].x, landmarks[p1].y)
        x2, y2 = (landmarks[p2].x, landmarks[p2].y)
        x3, y3 = (landmarks[p3].x, landmarks[p3].y)

        angle = math.degrees(math.atan2(y3-y2, x3-x2) - math.atan2(y1-y2, x1-x2))
        angle = abs(angle)

        if angle > 180:
            angle = 360 - angle
        return angle