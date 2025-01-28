from abc import ABC, abstractmethod

# Estratégia para modos de execução
class ModeStrategy(ABC):
    @abstractmethod
    def should_terminate(self, elapsed_time, repetitions, max_duration, max_repetitions):
        pass