import cv2
import mediapipe as mp

class VideoProcessor:
    def __init__(self, source=0, display_name="Exercise"):
        self.capture = cv2.VideoCapture(source)
        self.display_name = display_name
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils

    # PROCESSA O FRAME E RETORNA AS COORDENADAS DAS LANDMARKS
    def process_frame(self, pose_detector):
        success, image = self.capture.read()
        if not success:
            return None, None

        image = cv2.resize(image, (640, 480))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose_detector.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        return image, results.pose_landmarks

    # DESENHA AS LANDMARKS NO FRAME ATUAL
    def draw_landmarks(self, image, landmarks):
        if landmarks:
            self.mp_drawing.draw_landmarks(
                image, 
                landmarks, 
                self.mp_pose.POSE_CONNECTIONS
            )
        return image

    # EXIBE O FRAME NA TELA EXIBINDO O FEEDBACK DA ANALISE DOS MOVIMENTOS
    def display_frame(self, image, feedback_text=None, color=(0, 255, 0)):
        if feedback_text:
            cv2.putText(
                image, 
                feedback_text, 
                (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                1.2, 
                color, 
                2
            )
        cv2.imshow(self.display_name, image)

    # LIBERA A CAPTURA DE VIDEO DO OPENCV E FECHA A JANELA DE EXIBICAO
    def release(self):
        self.capture.release()
        cv2.destroyAllWindows()