from Exercises.IExercise import Exercise
import time

class AbdominalRowerExercise(Exercise):
    def __init__(self):
        self.repetitions = 0
        self.last_position = False  # Para evitar contar múltiplas vezes a mesma posição
        self.last_print_time = 0
        self.print_interval = 0.5

    def get_exercise_name(self):
        return "Abdominal Remador"

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val

    def check_position(self, landmarks):
        try:
            # Calcular ângulos
            elbow_angle = self.find_angle(landmarks.landmark, 12, 14, 16)
            left_elbow_angle = self.find_angle(landmarks.landmark, 11, 13, 15)
            hip_angle = self.find_angle(landmarks.landmark, 11, 23, 25)
            left_hip_angle = self.find_angle(landmarks.landmark, 12, 24, 26)
            knee_angle = self.find_angle(landmarks.landmark, 23, 25, 27)
            left_knee_angle = self.find_angle(landmarks.landmark, 24, 26, 28)
            trunk_angle = self.find_angle(landmarks.landmark, 11, 23, 24)

            # Print dos ângulos no terminal
            current_time = time.time()
            if current_time - self.last_print_time >= self.print_interval:
                print("\n" + "="*50)
                print(f"Cotovelo Direito: {elbow_angle:.1f}°")
                print(f"Cotovelo Esquerdo: {left_elbow_angle:.1f}°")
                print(f"Quadril Direito: {hip_angle:.1f}°")
                print(f"Quadril Esquerdo: {left_hip_angle:.1f}°")
                print(f"Joelho Direito: {knee_angle:.1f}°")
                print(f"Joelho Esquerdo: {left_knee_angle:.1f}°")
                print(f"Tronco: {trunk_angle:.1f}°")
                print("="*50)
                self.last_print_time = current_time

            # Posição final (sentado) - quando atinge esta posição, conta uma repetição
            correct_position = (
                self.is_within_range(elbow_angle, 150, 180) and     # Braços estendidos
                self.is_within_range(left_elbow_angle, 130, 180) and
                self.is_within_range(hip_angle, 25, 50) and         # Quadril flexionado
                self.is_within_range(left_hip_angle, 25, 50) and
                self.is_within_range(knee_angle, 25, 50) and        # Joelhos flexionados
                self.is_within_range(left_knee_angle, 20, 50) and
                self.is_within_range(trunk_angle, 15, 40)           # Tronco mais vertical
            )

            # Lógica de contagem simplificada
            if correct_position and not self.last_position:
                self.repetitions += 1
                print(f"\nBOA! Repetição {self.repetitions} completada! 🎯")
                self.last_position = True
            elif not correct_position:
                self.last_position = False

            # Debug das posições
            if current_time - self.last_print_time >= self.print_interval:
                print(f"Posição correta: {correct_position}")
                print(f"Repetições: {self.repetitions}")

            # Feedback para a tela
            if correct_position:
                return True, f"CORRETO! - Repeticoes: {self.repetitions}"
            else:
                return False, f"Repeticoes: {self.repetitions}"

        except Exception as e:
            print(f"\nERRO: {str(e)}")
            return False, f"Erro ao calcular ângulos: {str(e)}"