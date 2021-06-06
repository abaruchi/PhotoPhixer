from datetime import datetime

from PhotoPhixer.common.config import SysConfig
from pony.orm import (Database, Optional, PrimaryKey, Required, Set)


def create_connection(config: SysConfig) -> Database:
    return Database(config.db_engine, str(config.db_file), create_db=True)


class File(create_connection.Entity):
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


class Directory(create_connection.Entity):
    id = PrimaryKey(str)
    path = Required(str)
    date_creation = Required(datetime)
    last_update = Optional(datetime)
    files = Set(File)


create_connection.generate_mapping(create_tables=True)
