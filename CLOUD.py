import requests
from bs4 import BeautifulSoup
import re
import smtplib
import time

site= "https://in.bookmyshow.com/buytickets/shaapit-stree-bhiwadi/movie-bhwd-ET00096441-MT/20190422"
date="20190431"
site = site+date
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

venue ='SRBR'
show='10:00 AM'
delay=300

TO = 'gopi.krishna.16cse@bml.edu.in'

GMAIL_USER = 'saikrishna2290@gmail.com'
GMAIL_PASS = 'saikrishna321'
SUBJECT = 'Tickets are now available, Book fast'
TEXT = 'The tickets are now available for the ' + show + ' show at the venue ' +venue

def send_email():
    print("Sending Email")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'
    print(header)
    msg = header + '\n' + TEXT + ' \n\n'
    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()


req = requests.get(site, headers=hdr)
soup = BeautifulSoup(req.text, 'html.parser')
soup2 = soup.find_all('div', {'data-online': 'Y'})
line = str(soup2)
soup3= BeautifulSoup(line, 'html.parser')
soup4=soup3.find_all('a', {'data-venue-code': venue})
line1=str(soup4)
soup5=BeautifulSoup(line1, 'html.parser')
soup6=soup3.find_all('a', {'data-display-showtime': show})
line2=str(soup6)
result=re.findall('data-availability="A"',line2)
if len(result)>0:
    print("Available")
    send_email()
else :
    print("Not avail")