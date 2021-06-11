from abc import ABC, abstractmethod
from PhotoPhixer.storage.SQLite import models
from PhotoPhixer.common.config import SysConfig


class Durable(ABC):

    @abstractmethod
    def get_file(self, file_name: str, conf: SysConfig) -> dict:
        pass

    @abstractmethod
    def store_file(self, file_data: dict, conf: SysConfig) -> None:
        pass

    @abstractmethod
    def list_all_files(self, conf: SysConfig) -> dict:
        pass


class SQLiteStore(Durable):

    def get_file(self, file_name: str, conf: SysConfig) -> dict:
        pass

    def store_file(self, file_data: dict, conf: SysConfig) -> None:
        pass

    def list_all_files(self, conf: SysConfig) -> dict:
        pass


def interface_create(interface_type: str) -> Durable:
    pass
