from Exercises.IExercise import Exercise

class AbdominalRowerExercise(Exercise):
    def get_exercise_name(self):
        return "Abdominal Remador"

    def check_position(self, landmarks):

        # Calcular ângulos para a posição do exercício
        elbow_angle = self.find_angle(landmarks.landmark, 12, 14, 16)  # Braço direito
        left_elbow_angle = self.find_angle(landmarks.landmark, 11, 13, 15)  # Braço esquerdo
        hip_angle = self.find_angle(landmarks.landmark, 11, 23, 25)  # Quadril direito
        left_hip_angle = self.find_angle(landmarks.landmark, 12, 24, 26)  # Quadril esquerdo
        knee_angle = self.find_angle(landmarks.landmark, 23, 25, 27)  # Joelho direito
        left_knee_angle = self.find_angle(landmarks.landmark, 24, 26, 28)  # Joelho esquerdo
        trunk_angle = self.find_angle(landmarks.landmark, 11, 12, 24)  # Ângulo do tronco
        shoulder_angle = self.find_angle(landmarks.landmark, 11, 13, 14)  # Ângulo do ombro direito

        # Verificar se os ângulos estão dentro da faixa correta
        elbows_correct = (70 <= elbow_angle <= 110) and (70 <= left_elbow_angle <= 110)
        hips_correct = (90 <= hip_angle <= 120) and (90 <= left_hip_angle <= 120)
        knees_correct = (70 <= knee_angle <= 100) and (70 <= left_knee_angle <= 100)
        trunk_correct = (15 <= trunk_angle <= 45)  # Ajuste para flexão do tronco
        shoulders_correct = (150 <= shoulder_angle <= 180)  # Ombros em uma boa posição

        # Fornecer feedback com base na posição detectada
        if not elbows_correct:
            return False, "Mantenha os cotovelos dobrados corretamente (70-110 graus)"
        elif not hips_correct:
            return False, "Mantenha o quadril em uma posição correta (90-120 graus)"
        elif not knees_correct:
            return False, "Certifique-se de que os joelhos estão corretamente dobrados (70-100 graus)"
        elif not trunk_correct:
            return False, "O tronco deve estar inclinado corretamente (15-45 graus)"
        elif not shoulders_correct:
            return False, "Mantenha os ombros em uma posição correta (150-180 graus)"
        
        return True, "Posição correta!"

        # # Calculate angles for the rower position
        # elbow_angle = self.find_angle(landmarks.landmark, 12, 14, 16)  # Right arm
        # left_elbow_angle = self.find_angle(landmarks.landmark, 11, 13, 15)  # Left arm
        # hip_angle = self.find_angle(landmarks.landmark, 11, 23, 25)  # Right hip
        # left_hip_angle = self.find_angle(landmarks.landmark, 12, 24, 26)  # Left hip
        # knee_angle = self.find_angle(landmarks.landmark, 23, 25, 27)  # Right leg
        # left_knee_angle = self.find_angle(landmarks.landmark, 24, 26, 28)  # Left leg

        # # Check if angles are within the correct ranges
        # elbows_correct = (70 <= elbow_angle <= 110) and (70 <= left_elbow_angle <= 110)
        # hips_correct = (90 <= hip_angle <= 120) and (90 <= left_hip_angle <= 120)
        # knees_correct = (70 <= knee_angle <= 100) and (70 <= left_knee_angle <= 100)

        # # Provide feedback based on detected position
        # if not elbows_correct:
        #     return False, "Mantenha os cotovelos dobrados corretamente (70-110 graus)"
        # elif not hips_correct:
        #     return False, "Mantenha o quadril em uma posição correta (90-120 graus)"
        # elif not knees_correct:
        #     return False, "Certifique-se de que os joelhos estão corretamente dobrados (70-100 graus)"

        # return True, "Posição correta!"
