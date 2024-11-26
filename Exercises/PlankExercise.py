from Exercises.IExercise import Exercise

class PlankExercise(Exercise):
    def get_exercise_name(self):
        return "Prancha Abdominal"

    def check_position(self, landmarks):
        # Calculo dos angulos
        elbow_angle = self.find_angle(landmarks.landmark, 12, 14, 16)
        left_elbow_angle = self.find_angle(landmarks.landmark, 11, 13, 15)
        hip_angle = self.find_angle(landmarks.landmark, 11, 23, 25)
        left_hip_angle = self.find_angle(landmarks.landmark, 12, 24, 26)
        knee_angle = self.find_angle(landmarks.landmark, 23, 25, 27)
        left_knee_angle = self.find_angle(landmarks.landmark, 24, 26, 28)
        
        # Verifica se angulos estao corretos
        elbows_correct = (85 <= elbow_angle <= 115) or (85 <= left_elbow_angle <= 115)
        hips_correct = (hip_angle >= 115) or (left_hip_angle >= 115)
        knees_correct = (knee_angle >= 120) or (left_knee_angle >= 120)

        # Retorno
        if not elbows_correct:
            return False, "Ajuste os cotovelos (90 graus)"
        elif not hips_correct:
            return False, "Mantenha o quadril alinhado"
        elif not knees_correct:
            return False, "Mantenha as pernas retas"
        
        return True, "Posicao correta!"