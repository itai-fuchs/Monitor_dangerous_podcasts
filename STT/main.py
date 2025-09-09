from mongo_dal import MongoDAL
from elastic_dal import EsDAL
from STT import AudioTranscriber
import io

#Initializing the shows
stt=AudioTranscriber()
mongo_cli=MongoDAL()
es=EsDAL()


files_id = mongo_cli.get__all_files_id()

#Loops through. Pulls audio files from Mongo, transcribes them,
# and adds them to the same id in Elasticsearch.

for _id in files_id:

    file=mongo_cli.get_file_by_id(_id)
    audio_bytes = file.read()
    audio_stream = io.BytesIO(audio_bytes)
    text=stt.transcribe(audio_stream)
    es.update_file(_id,text)





