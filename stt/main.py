from mongo_dal import MongoDAL
from elastic_dal import EsDAL
from stt import AudioTranscriber
import io

#Initializing the DB conn
mongo_cli=MongoDAL()
es=EsDAL()

##Initializing the AudioTranscriber
stt=AudioTranscriber()

#get docs ids from MONGO
files_id = mongo_cli.get__all_docs_id()

#Pulls audio files from Mongo, transcribes them,
# and adds them to the same id in Elasticsearch.

for _id in files_id:

    file=mongo_cli.get_doc_by_id(_id)
    audio_bytes = file.read()
    audio_stream = io.BytesIO(audio_bytes)
    text=stt.transcribe(audio_stream)
    es.update_document(_id,text)




