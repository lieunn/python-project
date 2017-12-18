from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from pyelasticsearch import ElasticSearch
from datetime import datetime
con = Elasticsearch('http://127.0.0.1:9201', timeout=15)
es = IndicesClient(con)

if __name__ == '__main__':
    i = 1
    temp = []
    for hit in sorted(es.get_alias(expand_wildcards='all').keys(), reverse=True):
        #if    hit[0:9] == 'logstash-':
	if    hit[0:7] == 'kibana-':
	#if    hit[0:11] == 'vod_access-':
           temp.append(hit)
	if hit not in set([".kibana", "daily", "kibana-int"]) and hit[0:10] != 'vod_access':
		i = i + 1
 	

    for hit in sorted(temp):
        #print hit
        try:
            #print hit
            es.open(hit)
        except:
            pass

