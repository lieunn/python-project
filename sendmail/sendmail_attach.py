#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = 'ngoclieuspkt88@gmail.com'
toaddr = 'ngoclieusa@gmail.com'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Email Alert System Error'

body = 'CPU Server Kibana highload value is 90%'

msg.attach(MIMEText(body, 'plain'))

filename = 'thon ke so lieu metric'
attachment = open('/opt/scripts/solieu.txt', 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s'
                % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, '09910042')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print "Send mail Done"
