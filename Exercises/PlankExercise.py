# Sistema de Análise de Postura para Exercícios
#
# Integrantes:
#   João Victor Ferrareis Ribeiro
#   Mateus Lannes Cunha
#   Miguel Malini Louvem
#   Perseu Fernandes Machado de Oliveira
#

import time
from Exercises.IExercise import Exercise

class PlankExercise(Exercise):
    def __init__(self):
        self.repetitions = 0  # Zero, pois é baseado em tempo
        self.calories = 0.2   # Calorias por segundo
        self.last_print_time = 0
        self.print_interval = 0.5

    def get_exercise_name(self):
        return "Prancha Abdominal"
    
    def get_calories(self, elapsed_time):
        return self.calories * elapsed_time

    def check_position(self, landmarks):
        # Calculo dos angulos
        elbow_angle = self.find_angle(landmarks.landmark, 12, 14, 16)
        left_elbow_angle = self.find_angle(landmarks.landmark, 11, 13, 15)
        hip_angle = self.find_angle(landmarks.landmark, 11, 23, 25)
        left_hip_angle = self.find_angle(landmarks.landmark, 12, 24, 26)
        knee_angle = self.find_angle(landmarks.landmark, 23, 25, 27)
        left_knee_angle = self.find_angle(landmarks.landmark, 24, 26, 28)
        
        # Verifica se angulos estao corretos
        elbows_correct = (85 <= elbow_angle <= 120) or (85 <= left_elbow_angle <= 120)
        hips_correct = (hip_angle >= 115) or (left_hip_angle >= 115)
        knees_correct = (knee_angle >= 120) or (left_knee_angle >= 120)

        # Prints para acompanhamento
        current_time = time.time()
        if current_time - self.last_print_time >= self.print_interval:
            print("\n" + "="*50)
            print(f"Elbow Angle: {elbow_angle:.2f}, Left Elbow Angle: {left_elbow_angle:.2f}")
            print(f"Hip Angle: {hip_angle:.2f}, Left Hip Angle: {left_hip_angle:.2f}")
            print(f"Knee Angle: {knee_angle:.2f}, Left Knee Angle: {left_knee_angle:.2f}")
            print("="*50)
            self.last_print_time = current_time

        # Retorno
        if not elbows_correct:
            return False, "Ajuste os cotovelos (90 graus)"
        elif not hips_correct:
            return False, "Mantenha o quadril alinhado"
        elif not knees_correct:
            return False, "Mantenha as pernas retas"
        
        return True, "Posicao correta!"