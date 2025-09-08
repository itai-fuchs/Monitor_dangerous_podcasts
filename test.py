#
#
#
# from pymongo import MongoClient
#
# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017")
#
# # Select your database (replace 'your_database' with the actual database name)
# db = client['your_database']
#
# import gridfs
#
# # Create a GridFS object for the selected database
# fs = gridfs.GridFS(db)
#
# # Define the file path you want to upload
# file_path = "C:\podcasts\download (10).wav"
#
# # Open the file and upload it
# with open(file_path, 'rb') as file_data:
#     file_id = fs.put(file_data, filename='file.txt', description='Sample text file')
#
# print(f"File uploaded with file_id: {file_id}")
#
# # # Fetch the file using its filename
# file_data = fs.find_one({'filename': 'file.txt'})
#
# if file_data:
#     # Save the file to disk
#     with open("C:\podcasts\itai.wav", 'wb') as output_file:
#         output_file.write(file_data.read())
#     print("File downloaded successfully")
# else:
#     print("File not found")

from faster_whisper import WhisperModel

class AudioTranscriber:
    def __init__(self, model_size="tiny"):
        # מודלים: tiny, base, small, medium, large
        self.model = WhisperModel(model_size)

    def transcribe(self, file_path: str) -> str:
        segments, info = self.model.transcribe(file_path)
        text= " "
        for segment in segments:
            text += segment.text + "\n"
        return text.strip()


if __name__ == "__main__":
    transcriber = AudioTranscriber()
    text = transcriber.transcribe("C:/Users/itai/Downloads/Lady Gaga, Bruno Mars - Die With A Smile (Official Music Video).mp3")
    print("Transcribed text:")
    print(text)
