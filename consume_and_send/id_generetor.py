import hashlib
import json

def add_content_hash_id(data, length=10):
   data_str = json.dumps(data, sort_keys=True)
   hash_id = hashlib.sha256(data_str.encode()).hexdigest()[:length]
   data["id"] = hash_id
   return data
