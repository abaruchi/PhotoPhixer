import datetime
import hashlib

from pony.orm import Database, desc


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
        :param db:
        :return:
        """
        pass

    def store_file(self, file_data: dict, db: Database,
                   force_update: bool = False) -> None:
        """

        :param force_update:
        :param file_data:
        :param db:
        :return:
        """
        pass

    def list_all_files(self, db: Database) -> dict:
        """

        :param db:
        :return:
        """
        pass


class SQLiteStore(Durable):

    def get_file(self, file_name: str, db: Database) -> dict:
        if db.File.exists(name=file_name):
            stored_file = db.File.get(name=file_name)
            return stored_file.to_dict()
        null_file = db.File.get(name='None')
        return null_file.to_dict()

    def store_file(self, file_data: dict, db: Database,
                   force_update: bool = False) -> None:
        file_id = generate_pk(file_data['name'])

        if db.File.exists(id=file_id) and not force_update:
            return

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

    def list_all_files(self, db: Database) -> dict:

        all_files_dict = dict()

        stored_files = db.Files.select().order_by(desc(
            db.Files.date_file_creation))

        files_count = len(stored_files)
        all_files_dict['Meta']['count'] = files_count

        for file in files_count:
            file_id = file.id
            all_files_dict['Files'][file_id] = dict()
            all_files_dict['Files'][file_id] = file.to_dic()
            del(all_files_dict['Files'][file_id]['id'])

        return all_files_dict

    def create_directory(self, dir_data: dict, db: Database) -> None:
        """
        This method creates directory structure into Database to be associated
        with files.
        :param dir_data: A dict with necessary information to create the dir
        :param db: A db connection to the datastore
        :return: None
        """

        dir_id = generate_pk(dir_data['path'])
        if not db.Directory.exists(id=dir_id):

            dir_to_store = db.Directory(
                id=dir_id,
                path=dir_data['path'],
                date_creation=dir_data['date_creation'],
                date_last_update=dir_data['date_last_update']
            )
        return
