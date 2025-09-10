from decrypter import Decrypter
import config
from elastic_dal import EsDAL
from text_analysis import TextAnalysis

# create Elastic connector object
es=EsDAL()

#Receives 2 lists of dangerous words
hostile_list=Decrypter.decoding(config.HOSTILE_LIST)
les_hostile_list=Decrypter.decoding(config.LES_HOSTILE_LIST)



#For each document, it receives its stt, performs calculations on it,
# and adds them to the document.

for doc in es.get_documents_filed("stt"):
    text=doc[1]
    _id=doc[0]
    if text:

        #Adds a risk percentage
        risk_percent=TextAnalysis(text,hostile_list,les_hostile_list).risk_percent()
        es.update_document_filed(_id,risk_percent)

        #Adds if is_criminal
        is_criminal = TextAnalysis(text, hostile_list, les_hostile_list).criminal_event()

        es.update_document_filed(_id, is_criminal)

        #Adds risk level
        risk_level = TextAnalysis(text, hostile_list, les_hostile_list).risk_level()

        es.update_document_filed(_id, risk_level)