from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from pyelasticsearch import ElasticSearch
from datetime import datetime

con = Elasticsearch('http://127.0.0.1:9201', timeout=15)
es = IndicesClient(con)
#deles = ElasticSearch('http://127.0.0.1:9201', timeout=15)

if __name__ == '__main__':
 indexs=[]
 default={}
 #indexs = ["logstash-2017.11.08", "vod_access-2017.11.12", "logstash-2017.11.09", "logstash-2017.11.10", "vod_access-2017.11.11"]
 for hit in sorted(es.get_alias(expand_wildcards='all').keys(), reverse=True):
     indexs.append(hit)
 for i in [x.split('-') for x in indexs]:
  #print i
  default[i[0]] = ['-'.join(y) for y in [x.split('-') for x in indexs] if y[0] == i[0]]


 for key, value in default.iteritems():
    
      if key == 'logstash':

	  for j in (value[10:]):
		es.close(j)

      elif key == 'kibana':

           for l in (value[5:]):
		 es.close(l)  
      else:

	   for k in (value[2:]):
		 es.close(k)
