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
                       'DROPBOX': {'access_key': "some_key_here",
                                   'device_dir_01': "'mobile_foo'",
                                   'device_match_01': "'device01'",
                                   'photo_path': '/Camera Uploads/'},
                       'GLOBAL': {'db_engine': 'sqlite',
                                  'debug': 'False',
                                  'log_file': '/var/log/',
                                  'sqlite_path': 'data/SQLite/photophixer.db',
                                  'temp_path': '/tmp/'}}
        self.assertDictEqual(self.configuration.list_config(), config_dict)
