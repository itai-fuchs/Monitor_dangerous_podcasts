import base64


class Decrypter:
    def __init__(self,text):
        self.text=text


    def decoding(self):
        #decode the string into bytes
        base64_bytes = self.text.encode('ascii')

        #encode the string as ASCII
        decoded_bytes = base64.b64decode(base64_bytes)

        #Decode the bytes into a string using UTF-8
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text


