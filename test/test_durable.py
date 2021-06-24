import unittest
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
        datetime_dir_01 = datetime(year=2020,
                                   month=1,
                                   day=1,
                                   hour=10,
                                   minute=00,
                                   second=00,
                                   microsecond=00)
        dir_01 = {
            'path': '/Camera Uploads/Device_01/',
            'date_creation': datetime_dir_01,
            'date_last_update': datetime_dir_01
        }

        self.durable.create_directory(dir_01, self.db_conn)
        self.assertTrue(self.db_conn.Directory.exists(path=dir_01['path']))

    def test_get_file(self):
        pass

    def test_create_file(self):
        pass

    def test_list_all_files(self):
        pass
