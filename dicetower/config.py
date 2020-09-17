import figenv


class Configuration(metaclass=figenv.MetaConfig):
    PROJECT_NAME = 'Dice Tower'

    ALLOW_ORIGIN = ['dicetower.app']
    ALLOW_ORIGINS_RND = [
        'http://localhost:8000',
        'http://localhost:8080',
    ]
