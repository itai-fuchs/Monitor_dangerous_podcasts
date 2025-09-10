from decrypter import Decrypter
import config
from elastic_dal import EsDAL
from text_analysis import TextAnalysis

es=EsDAL()

hostile_list=Decrypter.decoding(config.HOSTILE_LIST)
les_hostile_list=Decrypter.decoding(config.LES_HOSTILE_LIST)




for _id in es.get_all_document_ids():
    text=es.get_document_filed(_id,"stt")
    if text:
        risk_percent=TextAnalysis(text,hostile_list,les_hostile_list).risk_percent()
        es.update_document(_id,risk_percent)


        is_criminal = TextAnalysis(text, hostile_list, les_hostile_list).criminal_event()

        es.update_document(_id, is_criminal)

        risk_level = TextAnalysis(text, hostile_list, les_hostile_list).risk_level()

        es.update_document(_id, risk_level)






