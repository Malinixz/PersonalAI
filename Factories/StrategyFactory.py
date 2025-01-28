from Strategies.DefaultStrategy import DefaultStrategy
from Strategies.RepsModeStrategy import RepsModeStrategy
from Strategies.TimeModeStrategy import TimeModeStrategy


class StrategyFactory:
    @staticmethod
    def get_strategy(mode, max_duration=None, max_repetitions=None):
        if mode == "time":
            if max_duration is None:
                raise ValueError("Duração máxima (max_duration) é obrigatória para o modo 'tempo'")
            return TimeModeStrategy()
        elif mode == "repetitions":
            if max_repetitions is None:
                raise ValueError("Número máximo de repetições (max_repetitions) é obrigatório para o modo 'repeticao'")
            return RepsModeStrategy()
        elif mode == "default":
            return DefaultStrategy()
        else:
            raise ValueError(f"Modo '{mode}' não é válido. Escolha 'tempo' ou 'repeticao'.")
