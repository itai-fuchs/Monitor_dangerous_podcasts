from faster_whisper import WhisperModel
from logger import Logger
logger = Logger.get_logger(__name__)

class AudioTranscriber:
    def __init__(self, model_size="tiny"):
        self.model = WhisperModel(model_size)

    def transcribe(self, file_path):
        try:
            segments, info = self.model.transcribe(file_path)
            text= " "
            for segment in segments:
                text += segment.text + "\n"
            logger.info(f"info: STT file {file_path} successfully")
            return text.strip()
        except Exception as e:
            logger.error(f"ERROR: Failed to STT file {file_path}: {e}")



