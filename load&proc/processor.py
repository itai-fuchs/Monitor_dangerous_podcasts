import logging
from pprint import pprint

import config
from pathlib import Path
from datetime import datetime
logger = logging.getLogger(__name__)


class Processor:

    def __init__(self,file_path):
            self.file_path = file_path

   #Extract file metadata
    def metaData(self):
        try:
            file_stats =  self.file_path.stat()
            creation_time = datetime.fromtimestamp(file_stats.st_ctime)
            modification_time = datetime.fromtimestamp(file_stats.st_mtime)
            access_time = datetime.fromtimestamp(file_stats.st_atime)


            return {"File_name": self.file_path.name,
                  "File-stem": str(self.file_path.stem),
                  "File_suffix": str(self.file_path.suffix),
                  "Creation_Time": str(creation_time),
                  "Last_Modified": str(modification_time),
                    "Last_Accessed":str(access_time),
                  "file_size_bytes" : str(file_stats.st_size),
                  "file_size_mb": f"{str(file_stats.st_size / (1024 ** 2))[:4]}MB"

                  }

        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    #Building json
    def get_json(self):
        return {"path":str(self.file_path.parent),
                "metaData":self.metaData()}


