import requests
from datetime import datetime, timedelta
import json

default = """curl -XPUT 'localhost:9200/twitter?pretty' -H 'Content-Type: application/json' -d'
{
    "settings" : {
        "index" : {
            "number_of_shards" : 3, 
            "number_of_replicas" : 2 
        }
    }
}
'
"""

for i in range(2, 100):
        index_name = 'logstash-' + str(datetime.now() + timedelta(days=-i))[0:10].replace('-','.')
        head = {"Content-Type":"application/json"}
        url = "http://127.0.0.1:9201/%s?pretty" %(index_name,) 
        #data = {"settings": {"index":{"number_of_shards":5, "number_of_replicas":1}}}
        r = requests.put(url, headers=head)
    

