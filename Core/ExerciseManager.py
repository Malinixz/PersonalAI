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

        # Check if the video source is valid
        if not cap.isOpened():
            print("Erro: Não foi possível abrir a câmera ou o vídeo.")
            return

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

                # No método run() do ExerciseManager, modifique a parte que mostra o feedback:
                if results.pose_landmarks:
                    correct_position, feedback = self.exercise.check_position(results.pose_landmarks)
                    feedback_color = (0, 255, 0) if correct_position else (0, 0, 255)
                    
                    # Aumentar o tamanho do texto do feedback
                    cv2.putText(image, feedback, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, feedback_color, 2, cv2.LINE_AA)

                cv2.imshow(self.exercise.get_exercise_name(), image)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()