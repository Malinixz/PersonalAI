from abc import ABC, abstractmethod

class PositionCheckStrategy(ABC):
    @abstractmethod
    def check_position(self, landmarks):
        """
        Verifica se a postura está correta com base nas landmarks.
        :param landmarks: Landmarks detectadas pelo MediaPipe.
        :return: Tuple (bool, str) indicando se a postura está correta e o feedback.
        """
        pass