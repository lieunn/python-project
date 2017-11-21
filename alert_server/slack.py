import sys
import os
import json
import requests
import exceptions
from flask import Flask
url = 'https://hooks.slack.com/services/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'
payload={"channel": "#alert-service", "username": "lieunn", "icon_emoji": ":fbox:"}
app = Flask(__name__)
@app.route('/alert_disk/')
def alert_disk():
 dict={}
 var="df / |awk '{ print $5}' |  awk 'NR==2'|cut -d '%' -f1"
 tmp=os.popen(var).read().rstrip("\n\r")
 disk="df / |awk '{ print $5}' |  awk 'NR==2'"
 dict["disk_value"]= os.popen(disk).read().rstrip("\n\r")
 ip = "ifconfig ens33 | grep 'inet\ ' |awk '{print $2}'"
 dict["ip_value"]=os.popen(ip).read().rstrip("\n\r")
 try:
	if int(tmp) > 85:
	 dict["message"]="Alert Disk Critical"
         a=json.dumps(dict,indent=2)
	 #a=json.dumps(dict,indent=2)
	 payload['text']=a
	 pljson = json.dumps(payload)
         print pljson
         r = requests.post(url, data= {'payload' : pljson})
	elif int(tmp) >= 60 and int(tmp) <= 85:
	 dict["message"]="Alert Disk Warning"
	 b=json.dumps(dict,indent=2)
	 payload['text']=b
	 pljson = json.dumps(payload)
	 r = requests.post(url, data= {'payload'  : pljson})
	else:
	 print "no problem"
 except  exceptions.NameError, e:
          print e
 return str(dict)

@app.route('/alert_ram/')
def alert_ram():
 dict={}
 var="free -m | awk 'NR==2{printf $3*100/$2 }'"
 mem_ulti="free -h | awk 'NR==2{printf $3}'"
 tmp=os.popen(var).read().rstrip("\n\r")
 #print float(tmp)
 #memory="free -m | awk 'NR==2{printf "Memory Usage: %s/%sMB (%.2f%)\n", $3,$2,$3*100/$2 }'|awk '{print $4}'|tr -d '()'"
 dict["memory_percent"]= os.popen(var).read().rstrip("\n\r")+"%"
 dict["memory_value"]= os.popen(mem_ulti).read().rstrip("\n\r")
 #print dict["memory_value"]
 ip = "ifconfig ens33 | grep 'inet\ ' |awk '{print $2}'"
 dict["ip_value"]=os.popen(ip).read().rstrip("\n\r")
 try:
        if float(tmp) > 85:
         dict["message"]="Alert Ram Critical"
         a=json.dumps(dict,indent=2)
         #a=json.dumps(dict,indent=2)
         payload['text']=a
         pljson = json.dumps(payload)
         print pljson
         r = requests.post(url, data= {'payload' : pljson})
        elif float(tmp) >= 60 and float(tmp) <= 85:
         dict["message"]="Alert Ram Warning"
         b=json.dumps(dict,indent=2)
         payload['text']=b
         pljson = json.dumps(payload)
         r = requests.post(url, data= {'payload'  : pljson})
        else:
         print "no problem"
 except  exceptions.NameError, e:
         print e
 return str(dict)

@app.route('/alert_cpu/')
def alert_cpu():
 dict={}
 cpu_sys="top -b -n 1 |grep -i '%Cpu(s)'|cut -d ',' -f2|awk '{print $1}'"
 var1=os.popen(cpu_sys).read().rstrip("\n\r")
 cpu_us="top -b -n 1 |grep -i '%Cpu(s)'|cut -d ',' -f1|awk '{print $2}'"
 var2=os.popen(cpu_us).read().rstrip("\n\r")
 cpu_ulti=float(var1)+ float(var2)
 dict["cpu_value"]=str(cpu_ulti).rstrip("\n\r")+ "%"
 ip = "ifconfig ens33 | grep 'inet\ ' |awk '{print $2}'"
 dict["ip_value"]=os.popen(ip).read().rstrip("\n\r")
 try:
        if int(cpu_ulti) > 85:
         dict["message"]="Alert CPU Critical"
         a=json.dumps(dict,indent=2)
         payload['text']=a
         pljson = json.dumps(payload)
         print pljson
         r = requests.post(url, data= {'payload' : pljson})
        elif int(cpu_ulti) >= 60 and int(tmp) <= 85:
         dict["message"]="Alert CPU Warning"
         b=json.dumps(dict,indent=2)
         payload['text']=b
         pljson = json.dumps(payload)
         r = requests.post(url, data= {'payload'  : pljson})
        else:
         print "no problem"
 except  exceptions.NameError, e:
          print e
 return str(dict)

if __name__ == '__main__':
   app.run(host='192.168.175.133',port='8888')
