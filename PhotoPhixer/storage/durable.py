from PhotoPhixer.storage.SQLite import models
from PhotoPhixer.common.config import SysConfig
import hashlib


def generate_pk(file_path: str) -> str:
    """
    Generates a string that represents the md5 hash of filename
    :param file_path: The file path in Dropbox to create the hash
    :return: MD5 hash to use as PK to store locally
    """
    file_path_md5 = hashlib.md5(file_path.encode())
    return file_path_md5.hexdigest()


class Durable(object):

    def get_file(self, file_name: str, conf: SysConfig, db) -> dict:
        pass

    def store_file(self, file_data: dict, conf: SysConfig, db) -> None:
        pass

    def list_all_files(self, conf: SysConfig, db) -> dict:
        pass


class SQLiteStore(Durable):

    def get_file(self, file_name: str, conf: SysConfig, db: ) -> dict:
        pass

    def store_file(self, file_data: dict, conf: SysConfig) -> None:
        pass

    def list_all_files(self, conf: SysConfig) -> dict:
        pass
