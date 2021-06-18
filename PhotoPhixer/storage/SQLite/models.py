from datetime import datetime

from PhotoPhixer.common.config import main_config, SysConfig
from pony.orm import (Database, Optional, PrimaryKey, Required, Set)


def create_db_connection(config: SysConfig) -> Database:
    """

    :param config:
    :return:
    """
    config_dict = config.list_config()
    return Database(
        config_dict['GLOBAL']['db_engine'],
        config_dict['GLOBAL']['sqlite_path'],
        create_db=True)




class File(create_db_connection.Entity):
    id = PrimaryKey(str)
    name = Optional(str)
    file_type = Optional(str)
    device = Optional(str)
    has_metadata = Optional(bool)
    date_processing = Optional(datetime)
    date_file_creation = Optional(datetime)
    date_last_change = Optional(datetime)
    dropbox_hash = Optional(str)
    directory = Optional('Directory')


class Directory(db.Entity):
    id = PrimaryKey(str)
    path = Required(str)
    date_creation = Required(datetime)
    last_update = Optional(datetime)
    files = Set(File)


db.generate_mapping(create_tables=True)
