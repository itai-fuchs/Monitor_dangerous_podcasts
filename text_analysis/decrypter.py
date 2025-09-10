import base64
from logger import Logger
logger = Logger.get_logger(__name__)
class Decrypter:

    @staticmethod
    def decoding(text):
        try:
            #decode the string into bytes
            base64_bytes = text.encode('ascii')

            #encode the string as ASCII
            decoded_bytes = base64.b64decode(base64_bytes)

            #Decode the bytes into text_analysis string using UTF-8
            decoded_text = decoded_bytes.decode('utf-8')

            logger.info("info: text decoding successfully")

            return decoded_text.lower().split(",")
        except Exception as e:
            logger.info(f"error: failed to decoding text: {e}")




