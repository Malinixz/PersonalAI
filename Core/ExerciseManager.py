import cv2
import mediapipe as mp
from Factories.ExerciseFactory import ExerciseFactory
import time
import numpy as np

class ExerciseManager:
    def __init__(self, exercise_type, video_path=0, mode="default", total_repetitions=None):
        self.exercise = ExerciseFactory.create_exercise(exercise_type)
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.video_path = video_path
        self.mode = mode
        self.total_repetitions = total_repetitions

    def run(self):
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print("Erro: Não foi possível abrir a câmera ou o vídeo.")
            return

        start_time = time.time()
        max_duration = 30 if self.mode == "time" else None

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

                if results.pose_landmarks:
                    correct_position, feedback = self.exercise.check_position(results.pose_landmarks)
                    feedback_color = (0, 255, 0) if correct_position else (0, 0, 255)
                    cv2.putText(image, feedback, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, feedback_color, 2, cv2.LINE_AA)

                cv2.imshow(self.exercise.get_exercise_name(), image)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

                elapsed_time = time.time() - start_time
                if self.mode == "time" and elapsed_time >= max_duration:
                    break
                if self.mode == "repetitions" and self.exercise.repetitions >= self.total_repetitions:
                    break

        elapsed_time = time.time() - start_time
        final_frame = self.display_final_metrics(self.exercise.repetitions, elapsed_time)

        # Exibe o frame final com as métricas por 5 segundos
        cv2.imshow("Resumo do Exercício", final_frame)
        cv2.waitKey(10000)

        cap.release()
        cv2.destroyAllWindows()

    def display_final_metrics(self, repetitions, elapsed_time):
        final_frame = (np.ones((480, 640, 3), dtype=np.uint8))  # Branco como fundo

        if self.mode == "time":
            reps_per_second = repetitions / 30
        elif elapsed_time > 0:
            reps_per_second = repetitions / elapsed_time
        else:
            reps_per_second = 0

        calories_burned = self.exercise.calories * repetitions
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
