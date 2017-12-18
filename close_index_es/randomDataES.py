import requests
from datetime import datetime, timedelta

default = """
curl -XPUT 'localhost:9200/twitter/tweet/1?pretty' -H 'Content-Type: application/json' -d'
{
    "user" : "kimchy",
    "post_date" : "2009-11-15T14:12:12",
    "message" : "trying out Elasticsearch"
}
'
"""

import json

for i in range(2, 100):
	index = 'logstash-' + str(datetime.now() + timedelta(days=-i))[0:10].replace('-','.')
	for i in range(1, 100):
		content = {"user": str(i), "message": "content for %s" %(str(i),)} 
		head = {"Content-Type":"application/json"}
		url = 'http://127.0.0.1:9201/' + index + '/fboxs/%s?pretty' %(str(i),)
		r = requests.put(url, data=json.dumps(content), headers=head)
