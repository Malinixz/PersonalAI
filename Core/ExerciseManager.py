import cv2
import mediapipe as mp
from Factories.ExerciseFactory import ExerciseFactory
import time
import numpy as np

class ExerciseManager:
    def __init__(self, exercise_type, video_path=0, mode="default", total_repetitions=None, max_duration=None):
        self.exercise = ExerciseFactory.create_exercise(exercise_type)
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.video_path = video_path
        self.mode = mode
        self.total_repetitions = total_repetitions
        self.max_duration = max_duration
        self.use_camera = video_path == 0  # Verifica se está usando câmera
        self.total_elapsed_time = 0
        self.start_time = 0
        self.is_paused = False

    def countdown_timer(self, cap):
        # Executa uma contagem regressiva de 3 segundos antes do início do exercício
        start_countdown = time.time()
        
        with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while time.time() - start_countdown < 3:
                success, image = cap.read()
                if not success:
                    print("Não foi possível receber o frame da câmera.")
                    return False

                image = cv2.resize(image, (640, 480))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Desenha os landmarks do corpo
                if results.pose_landmarks:
                    self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

                # Calcula o tempo restante do countdown
                time_left = 3 - int(time.time() - start_countdown)
                
                # Adiciona o texto de countdown na imagem
                cv2.putText(
                    image, 
                    f"Prepare-se! Iniciando em {time_left}", 
                    (50, 100), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1.2, 
                    (0, 255, 0), 
                    2, 
                    cv2.LINE_AA
                )

                # Adiciona instruções
                cv2.putText(
                    image, 
                    f"Exercício: {self.exercise.get_exercise_name()}", 
                    (50, 200), 
                    cv2.FONT_HERSHEY_SIMPLEX, 
                    1, 
                    (255, 0, 0), 
                    2, 
                    cv2.LINE_AA
                )

                cv2.imshow(self.exercise.get_exercise_name(), image)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    return False

        return True

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Erro: Não foi possível abrir a câmera ou o vídeo.")
            return

        # Adiciona o countdown APENAS para câmera
        if self.use_camera:
            if not self.countdown_timer(cap):
                cap.release()
                cv2.destroyAllWindows()
                return

            # Reinicia a captura de vídeo caso tenha sido usada durante o countdown
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.start_time = time.time()

        # Usa o tempo personalizado caso no modo "tempo"
        max_duration = self.max_duration if self.mode == "time" else None

        with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Não foi possível receber o frame da câmera.")
                    break

                image = cv2.resize(image, (640, 480))
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

                # Calcula o tempo decorrido
                current_time = time.time()
                if not self.is_paused:
                    self.total_elapsed_time = current_time - self.start_time

                if results.pose_landmarks:
                    correct_position, feedback = self.exercise.check_position(results.pose_landmarks)
                    feedback_color = (0, 255, 0) if correct_position else (0, 0, 255)
                    
                    # Adiciona o tempo junto com o feedback
                    feedback_text = f"Tempo: {self.total_elapsed_time:.1f}s | {feedback}"
                    cv2.putText(image, feedback_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, feedback_color, 2, cv2.LINE_AA)

                cv2.imshow(self.exercise.get_exercise_name(), image)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

                if self.mode == "time" and self.total_elapsed_time >= max_duration:
                    break
                if self.mode == "repetitions" and self.exercise.repetitions >= self.total_repetitions:
                    break

        final_frame = self.display_final_metrics(self.exercise.repetitions, self.total_elapsed_time)

        # Exibe o frame final com as métricas por 10 segundos
        cv2.imshow("Resumo do Exercício", final_frame)
        cv2.waitKey(10000)

        cap.release()
        cv2.destroyAllWindows()

    def display_final_metrics(self, repetitions, elapsed_time):
        final_frame = np.ones((480, 640, 3), dtype=np.uint8)  # Branco como fundo

        if elapsed_time > 0:
            reps_per_second = repetitions / elapsed_time
        else:
            reps_per_second = 0

        calories_burned = self.exercise.get_calories(elapsed_time)
        metrics = {
            "Repeticoes totais": repetitions,
            "Tempo total": f"{elapsed_time:.2f} segundos",
            "Calorias gastas": f"{calories_burned:.2f} kcal",
            "Repeticoes por segundo": f"{reps_per_second:.2f}"
        }

        y_offset = 50
        for key, value in metrics.items():
            text = f"{key}: {value}"
            cv2.putText(final_frame, text, (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            y_offset += 30

        return final_frame