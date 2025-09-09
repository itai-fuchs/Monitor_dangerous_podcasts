from decrypter import Decrypter
import config
from elastic_dal import EsDAL
from text_analysis import Text_analysis
es=EsDAL()


for _id in es.get_all_files_id():
    text=es.get_file_stt(_id,"stt")
    hostile_list=Decrypter.decoding(config.HOSTILE_LIST)

    les_hostile_list=Decrypter.decoding(config.LES_HOSTILE_LIST)

    analyze=Text_analysis(text,hostile_list,les_hostile_list)
    print(analyze.risk_percent())
