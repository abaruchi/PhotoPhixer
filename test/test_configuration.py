import unittest
from os import getcwd
from PhotoPhixer.common import config
from pathlib import Path


class TestConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.configuration = config.SysConfig()
        self.custom_db_file = Path(getcwd()) / 'test/db_dir/test_db_file.db'
        self.custom_log_file = Path(getcwd()) / 'test/log_dir/'

    def test_default_configuration(self):
        self.assertTrue(self.configuration.db_file.parent.exists())
        self.assertTrue(self.configuration.log_dir.exists())

    def test_custom_configuration(self):
        # Stores old config files to cleanup
        self.old_log_dir = self.configuration.log_dir
        self.old_db_file = self.configuration.db_file

        # Set custom configurations
        self.configuration.log_dir = str(self.custom_log_file)
        self.configuration.custom_db_file = str(self.custom_db_file)

        self.assertTrue(self.configuration.log_dir.exists())
        self.assertTrue(self.configuration.db_file.parent.exists())

    def tearDown(self) -> None:
        self.old_log_dir.rmdir()
        self.old_db_file.parent.rmdir()

        self.configuration.log_dir.rmdir()
        self.configuration.db_file.parent.rmdir()
