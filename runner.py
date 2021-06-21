"""
This script contains some ideas to how the
system gonna work - nothing here should
taken seriously
"""

from pathlib import Path

import dropbox
from exif import Image
from plum import UnpackError

# TOKEN = ''
#
# temp_dir = Path('/var/tmp/')
# dropbox_path = '/TestDir/'
#
# dbx = dropbox.Dropbox(TOKEN)
#
# '''
# For each file in Dropbox Folder
# 1. Download to a temp directory
# 2. Get metadata
# 3. Remove it from temp directory
# '''
#
# remote_files = dbx.files_list_folder(dropbox_path)
# for db_file in remote_files.entries:
#     local_file = temp_dir / db_file.name
#     dbx.files_download_to_file(str(local_file), db_file.path_display)
#
#     with local_file.open(mode='rb') as tf:
#         try:
#             image_file = Image(tf)
#             if image_file.has_exif:
#                 if 'model' in image_file.list_all():
#                     print("File: {}, Device: {}".format(local_file,
#                                                         image_file.model))
#                 else:
#                     print("File {} not identified".format(local_file))
#         except (ValueError, UnpackError):
#             print("Couldnt check metadata file {}".format(local_file))
#         local_file.unlink()
