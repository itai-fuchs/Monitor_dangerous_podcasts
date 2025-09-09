from pathlib import Path
from logger import Logger
logger = Logger.get_logger(__name__)


class DirectoryScanner:

    def __init__(self, directory):
        try:
            self.directory = Path(directory)
            logger.info(f"info: {self.directory} found successfully.")
        except FileNotFoundError:
            logger.error(f"Error: { self.directory} not found. Please ensure the file exists.")

    def get_files(self):
        """

    :return: all audio files in the parent directory
        """
        return [f for f in self.directory.iterdir() if f.is_file()and f.suffix.lower() == ".wav"]




