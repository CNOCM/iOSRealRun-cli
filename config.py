import yaml


class Config:

    def __init__(self, config_file="config.yaml"):
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)

        for key, value in config.items():
            setattr(self, key, value)


config = Config()
