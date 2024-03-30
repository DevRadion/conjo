import yaml


class Config(object):
    def __init__(self):
        self.load()

    _instance = None

    @staticmethod
    def shared():
        if Config._instance is None:
            Config._instance = Config()
        return Config._instance

    @property
    def log_level(self):
        return self._config["cli"].get("log_level", "DEBUG")

    @property
    def verbose(self):
        return self._config["cli"].get("verbose", "False")

    @property
    def wait_for_input(self):
        return self._config["cli"].get("wait_for_input", "False")

    def load(self):
        with open("config.yaml") as f:
            self._config = yaml.load(f, Loader=yaml.FullLoader)

    # Private
    _config = None
