from Strategies.IModeStrategy import ModeStrategy

class DefaultStrategy(ModeStrategy):
    def should_terminate(self, elapsed_time, repetitions, max_duration, max_repetitions):
        return False
