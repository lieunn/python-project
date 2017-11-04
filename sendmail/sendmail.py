#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = 'ngoclieuspkt88@gmail.com'
toaddr = 'ngoclieusa@gmail.com'
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Alert Metric System'

body = 'Metric Elastich Value is 12.3'
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, '09910042')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print " Send mail Done!"

			
