from Exercises.IExercise import Exercise  
import time

class PushUpExercise(Exercise):
    def __init__(self):
        self.repetitions = 0
        self.last_position = False  # Indica se a última posição foi a baixa
        self.is_valid_cycle = False  # Indica se o ciclo atual é válido
        self.last_print_time = 0
        self.print_interval = 0.5
        self.calories = 0.6    # Calorias por repetição

    def get_exercise_name(self):
        return "Flexão de Braço"

    def is_within_range(self, value, min_val, max_val):
        return min_val <= value <= max_val
    
    def get_calories(self, elapsed_time):
        return self.calories * self.repetitions

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
                self.is_within_range(left_elbow_angle, 50, 90) and  # Cotovelos dobrados
                self.is_within_range(right_elbow_angle, 50, 90)
            )

            # Lógica da posição alta
            position_up = (
                self.is_within_range(left_elbow_angle, 160, 180) and  # Braços esticados
                self.is_within_range(right_elbow_angle, 160, 180) and
                self.is_within_range(left_body_alignment, 155, 190) and  # Corpo alinhado
                self.is_within_range(right_body_alignment, 155, 190)
            )

            # Contagem de repetições
            if position_down and not self.last_position:
                self.last_position = True
                self.is_valid_cycle = True  # Inicia um ciclo válido
            elif position_up and self.last_position and self.is_valid_cycle:
                self.repetitions += 1
                print(f"\nBOA! Repetição {self.repetitions} completada!")
                self.last_position = False
                self.is_valid_cycle = False  # Conclui o ciclo válido
            elif position_up and not self.is_valid_cycle:
                print("\nAVISO: Ciclo inválido detectado. A repetição não foi contada.")

            # Feedback para a tela
            if position_up:
                return True, f"CORRETO! - Repeticoes: {self.repetitions}"
            elif position_down:
                return False, f"Repeticoes: {self.repetitions}"
            else:
                return False, f"Repeticoes: {self.repetitions}"

        except Exception as e:
            print(f"\nERRO: {str(e)}")
            return False, f"Erro ao calcular ângulos: {str(e)}"
