from os import getcwd
from pathlib import Path
from configparser import ConfigParser


class SysConfig(object):

    def __init__(self, config_file: Path = Path(getcwd()) / 'config.ini'):
        self.config_file = config_file

        if not self.config_file.exists():
            print(self.config_file)
            raise FileNotFoundError
        self.cp = ConfigParser()

    def list_config(self) -> dict:

        self.cp.read(str(self.config_file))
        all_config = dict()

        for section, values in self.cp.items():
            all_config[section] = dict()
            for conf, value in values.items():
                all_config[section][conf] = value

        return all_config


# This instantiation acts like a Singleton
main_config = SysConfig()
