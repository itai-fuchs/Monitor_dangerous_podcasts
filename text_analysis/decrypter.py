import base64

class Decrypter:

    @staticmethod
    def decoding(text):
        #decode the string into bytes
        base64_bytes = text.encode('ascii')

        #encode the string as ASCII
        decoded_bytes = base64.b64decode(base64_bytes)

        #Decode the bytes into text_analysis string using UTF-8
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text.lower().split(",")



