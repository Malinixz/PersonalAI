import cv2
import mediapipe as mp
from Factories.ExerciseFactory import ExerciseFactory

class ExerciseManager:
    def __init__(self, exercise_type, video_path=0):
        self.exercise = ExerciseFactory.create_exercise(exercise_type)
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.video_path = video_path

    def run(self):
        cap = cv2.VideoCapture(self.video_path)

        with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Não foi possível receber o frame da câmera.")
                    break

                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = pose.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

                if results.pose_landmarks:
                    correct_position, feedback = self.exercise.check_position(results.pose_landmarks)
                    # Adicione aqui a lógica para mostrar o feedback na tela

                cv2.imshow(self.exercise.get_exercise_name(), image)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()