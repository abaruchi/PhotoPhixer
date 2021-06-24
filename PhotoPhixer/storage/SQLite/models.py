from datetime import datetime
from pathlib import Path

from pony.orm import Database, Optional, PrimaryKey, Required, Set, db_session

from PhotoPhixer.common.config import SysConfig


def db_connection(config: SysConfig) -> Database:
    """
    This routine must be used to create and manage data in database.

    :param config: A config instance where important DB properties must be set
    :return: A database connection to handle data
    """
    config_dict = config.list_config()
    sqlite_path = Path(config_dict['GLOBAL']['sqlite_path'])

    db = Database(
        config_dict['GLOBAL']['db_engine'],
        str(sqlite_path),
        create_db=True)

    class File(db.Entity):
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
        date_last_update = Optional(datetime)
        files = Set(File)

    db.generate_mapping(create_tables=True)
    add_null_objects(db)

    return db


@db_session
def add_null_objects(db: Database) -> None:
    """
    This routine creates null objects into Database so we can return these
    objects instead of raising an error or different objects types.
    :param db: Database connection
    :return: None
    """

    if not db.File.exists(id='None'):
        null_file = db.File(
            id='None',
            name='None',
            file_type='None'
        )

    if not db.Directory.exists(id='None'):
        db.Directory(
            id='None',
            path='None',
            date_creation=datetime.now(),
            date_last_update=datetime.now(),
            files=null_file
        )
