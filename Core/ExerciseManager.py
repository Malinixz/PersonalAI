import cv2
import time
import mediapipe as mp

from Core.VideoProcessor import VideoProcessor
from Factories.StrategyFactory import StrategyFactory

class ExerciseManager:
    def __init__(self, exercise, video_path, mode="default", max_repetitions=None, max_duration=None):
        self.exercise = exercise
        self.video_processor = VideoProcessor(video_path, exercise.get_exercise_name())
        # self.mode = mode
        self.stop_strategy = StrategyFactory.get_strategy(mode) # Estrategia para parar a analise postural
        self.max_repetitions = max_repetitions
        self.max_duration = max_duration
        self.start_time = time.time()
        self.mp_pose = mp.solutions.pose

    def run(self):
        with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose_detector: # Instancia o detector de poses
            while True:
                image, landmarks = self.video_processor.process_frame(pose_detector)    # Processador de video gera as coordenadas das landmarks e as imagens
                
                if image is None:
                    break

                if landmarks:
                    correct_position, feedback = self.exercise.check_position(landmarks)    # Classe responsavel por analisar a postura retorna o feedback
                    
                    image = self.video_processor.draw_landmarks(image, landmarks)   # Landmarks sao desenhadas na imagem
                    self.video_processor.display_frame(  # Frame e exibido na tela com o feedback
                        image, 
                        feedback, 
                        color=(0, 255, 0) if correct_position else (0, 0, 255)
                    )

                if cv2.waitKey(25) & 0xFF == ord('q'):  # Quebra ao apertar Q
                    break

                elapsed_time = time.time() - self.start_time
                # if (self.mode == "time" and elapsed_time >= self.max_duration) or \
                #    (self.mode == "repetitions" and self.exercise.repetitions >= self.max_repetitions):
                #     break

                # Verifica se a sessao foi finalizada de acordo com a estrategia escolhida
                if self.stop_strategy.should_terminate(elapsed_time, self.exercise.repetitions, self.max_duration, self.max_repetitions):
                    break

        self.video_processor.release()