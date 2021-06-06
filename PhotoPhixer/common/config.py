from os import getcwd
from pathlib import Path


class SysConfig(object):

    def __init__(self):

        self.db_engine = 'sqlite'
        self.db_file = Path(getcwd()) / 'PhotoPhixer/data/SQLite/photophixer.db'
        self.log_dir = Path(getcwd()) / 'logs/'

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
        return self._db_engine

    @db_engine.setter
    def db_engine(self, value):
        self._db_engine = value

    @property
    def db_file(self):
        return self._db_file

    @db_file.setter
    def db_file(self, file_path: str):
        old_db_file = self.db_file
        self.db_file = Path(file_path)

        if not self.db_file.parent.exists():
            try:
                self.db_file.parent.mkdir(parents=True)
            except OSError:
                self.db_file = old_db_file
                print("Could not Create DB Dir {}".format(file_path))
                print("Kept Old DB Dir {}".format(self.db_file))

    @property
    def log_dir(self):
        return self._log_dir

    @log_dir.setter
    def log_dir(self, log_path: str):
        old_log_dir = self.log_dir
        self.log_dir = Path(log_path)

        if not self.log_dir.exists():
            try:
                self.log_dir.mkdir(parents=True)
            except OSError:
                self.log_dir = old_log_dir
                print("Could not Create Log Dir {}".format(log_path))
                print("Kept Old DB Dir {}".format(self.log_dir))


# Export the object SysConfig - Don't need to initialize it when using
sys_config = SysConfig()
