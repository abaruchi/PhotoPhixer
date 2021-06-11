import unittest
from os import getcwd
from PhotoPhixer.common import config
from pathlib import Path


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        test_file = Path(getcwd()) / 'test_config.ini'
        self.configuration = config.SysConfig(test_file)

    def test_config_dict(self):
        config_dict = {'DEFAULT': {},
                       'GLOBAL':
                           {'debug': 'False',
                            'dropbox_key': "'some_randon_key_here'",
                            'log_file': '/var/log/',
                            'sqlite_path': 'data/SQLite/photophixer.db',
                            'db_engine': 'sqlite',
                            'temp_path': '/tmp/',
                            'dropbox_photo_path': '/Camera Uploads/'}
                       }
        self.assertDictEqual(self.configuration.list_config(), config_dict)
