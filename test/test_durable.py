import unittest
import uuid
from datetime import datetime
from os import getcwd
from pathlib import Path

from pony.orm import db_session

from PhotoPhixer.common import config
from PhotoPhixer.storage import durable
from PhotoPhixer.storage.SQLite import models


class TestDurableSQLite(unittest.TestCase):

    def setUp(self) -> None:
        test_file = Path(getcwd()) / 'test_config.ini'
        test_config = config.SysConfig(test_file)
        self.db_conn = models.db_connection(test_config)
        self.durable = durable.SQLiteStore()

    def tearDown(self) -> None:
        self.db_conn.drop_all_tables(with_all_data=True)

    @db_session
    def test_create_directory(self):
        """

        :return:
        """
        dir_path = '/Camera Uploads/' + uuid.uuid4().hex.upper()[0:6]
        datetime_dir = datetime(year=2020,
                                month=1,
                                day=1,
                                hour=10,
                                minute=00,
                                second=00,
                                microsecond=00)
        dir_01 = {
            'path': dir_path,
            'date_creation': datetime_dir,
            'date_last_update': datetime_dir
        }
        self.durable.create_directory(dir_01, self.db_conn)
        self.assertTrue(self.db_conn.Directory.exists(path=dir_01['path']))

    @db_session
    def test_get_file(self):
        """

        :return:
        """
        datetime_file = datetime(year=2020,
                                 month=1,
                                 day=1,
                                 hour=10,
                                 minute=00,
                                 second=00,
                                 microsecond=00)

        file_name = uuid.uuid4().hex.upper()[0:6]
        file_01 = {
            'name': file_name,
            'file_type': 'photo',
            'device': 'device01',
            'has_metadata': 'True',
            'date_processing': datetime_file,
            'date_file_creation': datetime_file,
            'date_last_change': datetime_file,
            'dropbox_hash': 'some_hash_here'
        }
        self.durable.store_file(file_01, self.db_conn)

        self.assertEqual(
            self.durable.get_file('Test_File_01', self.db_conn),
            file_01['name'])

    def test_create_file(self):
        pass

    def test_list_all_files(self):
        pass
