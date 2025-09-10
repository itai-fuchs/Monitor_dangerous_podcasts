import uvicorn
from fastapi import FastAPI

from elastic_dal import EsDAL
import config



es = EsDAL().es
processing_done = False

#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     global processing_done
#     processing_done = False
#
#     yield

app = FastAPI()

@app.get("/is_criminal")
def is_criminal():
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"is_bds": "true"}},
                ]
            }
        },
        "size": 1000
    }

    res = es.search(index=config.ELASTIC_INDEX, body=query)

    return {"results": [hit["_source"] for hit in res["hits"]["hits"]]}

@app.get("/is_high_risk")
def is_high_risk():
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"bds_threat_level": "medium"}},
                ]
            }
        },
        "size": 1000
    }

    res = es.search(index=config.ELASTIC_INDEX, body=query)

    return {"results": [hit["_source"] for hit in res["hits"]["hits"]]}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.2", port=8001)