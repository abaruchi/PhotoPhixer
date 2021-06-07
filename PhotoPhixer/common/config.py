from os import getcwd
from pathlib import Path


class SysConfig(object):

    def __init__(self):

        self.__db_engine = 'sqlite'
        self.__db_file = Path(getcwd()) / 'PhotoPhixer/data/SQLite/photophixer.db'
        self.__log_dir = Path(getcwd()) / 'logs/'

        if not self.db_file.parent.exists():
            try:
                self.db_file.parent.mkdir(parents=True)
            except OSError as e:
                print("Error when creating Directory {}".format(
                    self.db_file.parent))
                print("Error: {}".format(e))

        if not self.log_dir.exists():
            try:
                self.log_dir.mkdir(parents=True)
            except OSError as e:
                print("Error when creating Directory {}".format(self.log_dir))
                print("Error: {}".format(e))

    @property
    def db_engine(self):
        return self.__db_engine

    @db_engine.setter
    def db_engine(self, value):
        self.__db_engine = value

    @property
    def db_file(self):
        return self.__db_file

    @db_file.setter
    def db_file(self, file_path: str):
        old_db_file = self.__db_file
        self.__db_file = Path(file_path)

        if not self.__db_file.parent.exists():
            try:
                self.__db_file.parent.mkdir(parents=True)
            except OSError:
                self.__db_file = old_db_file
                print("Could not Create DB Dir {}".format(file_path))
                print("Kept Old DB Dir {}".format(self.__db_file))

    @property
    def log_dir(self):
        return self.__log_dir

    @log_dir.setter
    def log_dir(self, log_path: str):
        old_log_dir = self.__log_dir
        self.__log_dir = Path(log_path)

        if not self.__log_dir.exists():
            try:
                self.__log_dir.mkdir(parents=True)
            except OSError:
                self.log_dir = old_log_dir
                print("Could not Create Log Dir {}".format(log_path))
                print("Kept Old DB Dir {}".format(self.__log_dir))


# Export the object SysConfig - Don't need to initialize it when using
sys_config = SysConfig()
