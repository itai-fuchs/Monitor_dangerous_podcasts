from pathlib import Path
import logging


logger = logging.getLogger(__name__)


class DirectoryScanner:
    '''
    create list of all files in directory
    '''
    def __init__(self, directory):
        try:
            self.directory = Path(directory)
        except FileNotFoundError:
            logger.error(f"Error: { self.directory} not found. Please ensure the file exists.")

    def get_files(self):

            return [f for f in self.directory.iterdir() if f.is_file()]




