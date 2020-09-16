import figenv


class Configuration(metaclass=figenv.MetaConfig):
    PROJECT_NAME = 'Dice Tower'

    ALLOW_ORIGIN = ['dicetower.app']
