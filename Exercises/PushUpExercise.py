from Exercises.IExercise import Exercise  
import time

class PushUpExercise(Exercise):
    def __init__(self):
        self.repetitions = 0
        self.last_position = False  
        self.last_print_time = 0
        self.print_interval = 0.5
        self.calories = 0.6    # Calorias por repetição

    def get_exercise_name(self):
        return "Flexão de Braço"

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val

    def check_position(self, landmarks):
        try:
            # Calcular ângulos
            left_elbow_angle = self.find_angle(landmarks.landmark, 11, 13, 15)  # Ombro -> Cotovelo -> Punho
            right_elbow_angle = self.find_angle(landmarks.landmark, 12, 14, 16)

            left_body_alignment = self.find_angle(landmarks.landmark, 11, 23, 25)  # Ombro -> Quadril -> Joelho
            right_body_alignment = self.find_angle(landmarks.landmark, 12, 24, 26)

            # Print dos ângulos no terminal
            current_time = time.time()
            if current_time - self.last_print_time >= self.print_interval:
                print("\n" + "=" * 50)
                print(f"Cotovelo Direito: {right_elbow_angle:.1f}°")
                print(f"Cotovelo Esquerdo: {left_elbow_angle:.1f}°")
                print(f"Alinhamento Corpo Direito: {right_body_alignment:.1f}°")
                print(f"Alinhamento Corpo Esquerdo: {left_body_alignment:.1f}°")
                print("=" * 50)
                self.last_print_time = current_time

            # Lógica da posição baixa
            position_down = (
                self.is_within_range(left_elbow_angle, 60, 90) and  # Cotovelos dobrados
                self.is_within_range(right_elbow_angle, 60, 90)
            )

            # Lógica da posição alta
            position_up = (
                self.is_within_range(left_elbow_angle, 160, 180) and  # Braços esticados
                self.is_within_range(right_elbow_angle, 160, 180) and
                self.is_within_range(left_body_alignment, 170, 190) and  # Corpo alinhado
                self.is_within_range(right_body_alignment, 170, 190)
            )

            # Contagem de repetições
            if position_down and not self.last_position:
                self.last_position = True
            elif position_up and self.last_position:
                self.repetitions += 1
                print(f"\nBOA! Repetição {self.repetitions} completada!")
                self.last_position = False

            # Feedback para a tela
            if position_up:
                return True, f"CORRETO! - Repetições: {self.repetitions}"
            elif position_down:
                return False, "Continue descendo..."
            else:
                return False, "Mantenha o corpo alinhado!"

        except Exception as e:
            print(f"\nERRO: {str(e)}")
            return False, f"Erro ao calcular ângulos: {str(e)}"
