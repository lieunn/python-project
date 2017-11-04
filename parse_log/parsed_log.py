import os.path
import json
import pymongo

def log_filter():
 file='metric.log'

 try:
	if os.path.isfile(file):
		content = []
       		with open(file, "r") as ins:
    			for str in ins:
        			tmp=str.split('-')[0] + str.split('- -')[1].split('[')[1].split(']')[0].split('+')[0] + "" + str.split('"')[1]
				b=tmp.split(' ')
        			a=["ip","time","method","description",'protocol']
				c=dict(zip(a,b))
        		content.append(json.dumps(c))
 	


    		with open("item.json", 'w+') as line:
			line.write('\n'.join(content))
         

 except IOError:
      print "file ko ton tai", file
def mongo():
  connection=pymongo.MongoClient("mongodb://localhost")
  db=connection.metric_box
  record=db.metric
  content = []
  with open("item.json", 'r') as lines:
	for line in lines:
		content.append(json.loads(line.strip()))	
  #f=open("item.json",'r')
  for item in content:
      	record.insert(item)

if __name__=="__main__":
   log_filter()
   mongo()
