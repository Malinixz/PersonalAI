# Estratégia para modo baseado em tempo
from Strategies.IModeStrategy import ModeStrategy

class TimeModeStrategy(ModeStrategy):
    def should_terminate(self, elapsed_time, repetitions, max_duration, max_repetitions):
        return elapsed_time >= max_duration