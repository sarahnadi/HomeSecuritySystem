import RPi.GPIO as gpio
import os
from picamera import PiCamera
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

fromaddr = "sarahnadi4@outlook.fr"
toaddr = "sarahnadi4@gmail.com"

mail = MIMEMultipart()

mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Attachment"
body = "Please find the attachment"

    
def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print (data)
    dat='%s.jpg'%data
    print (dat)
    attachment = open(dat, 'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP('smtp-mail.outlook.com', 25)
    server.starttls()
    server.login('sarahnadi4@outlook.fr', 'Veillance15')
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    time.sleep(5)
    print (data)
    camera.capture('%s.jpg'%data)
    time.sleep(1)
    sendMail(data)
    

camera = PiCamera()

#GPIO configuration
led=17
pir=18
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)            # initialize GPIO Pin as outputs
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input

while 1:
    if gpio.input(pir)==1:
        gpio.output(led, gpio.HIGH)
        capture_image()
        while(gpio.input(pir)==1):
            time.sleep(1)
        
    else:
        gpio.output(led, gpio.LOW)
        time.sleep(0.01)






