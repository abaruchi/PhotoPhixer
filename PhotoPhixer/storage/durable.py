import datetime
import hashlib

from PhotoPhixer.common.config import SysConfig
from pony.orm import Database


def generate_pk(file_name: str) -> str:
    """
    Generates a string that represents the md5 hash of filename
    :param file_name: The file path in Dropbox to create the hash
    :return: MD5 hash to use as PK to store locally
    """
    file_path_md5 = hashlib.md5(file_name.encode())
    return file_path_md5.hexdigest()


class Durable(object):

    def get_file(self, file_name: str, db: Database) -> dict:
        """

        :param file_name:
        :param conf:
        :param db:
        :return:
        """
        pass

    def store_file(self, file_data: dict, db: Database,
                   force_update: bool = False) -> None:
        """

        :param force_update:
        :param file_data:
        :param conf:
        :param db:
        :return:
        """
        pass

    def list_all_files(self, db: Database) -> dict:
        """

        :param conf:
        :param db:
        :return:
        """
        pass


class SQLiteStore(Durable):

    def get_file(self, file_name: str, db: Database) -> dict:
        if db.File.exists(name=file_name):
            stored_file = db.File.get(name=file_name)
            return stored_file.to_dict()
        null_file = stored_file = db.File.get(name='None')
        return null_file.to_dict()

    def store_file(self, file_data: dict, db: Database,
                   force_update: bool = False) -> None:
        file_id = generate_pk(file_data['name'])

        if db.File.exists(id=file_id) and not force_update:
           pass

        else:
            file_to_store = db.File(
                id=file_id,
                name=file_data['name'],
                file_type=file_data['file_type'],
                device=file_data['device'],
                has_metadata=file_data['has_metadata'],
                date_processing=file_data['date_processing'],
                date_file_creation=file_data['date_file_creation'],
                date_last_change=datetime.datetime.now(),
                dropbox_hash=file_data['dropbox_hash'],
                directory=file_data['directory'])



            )

    def list_all_files(self, db: Database) -> dict:
        pass
