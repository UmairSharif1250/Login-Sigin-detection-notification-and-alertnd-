from gpiozero import MotionSensor ,Button ,LED
from Picamera import Picamera
from email.mime.multipart import MIMEMultipart
from subprocess import call



import cv2

import os
import email.mime.application
import datetime
import smtplib
from time import sleep

#creating object for PIR Camera LEd
pir=MotionSensor(20)
camera=Picamera()
led=LED(17)
button=Button(16)

#Replace these 3 lines with our credential

from_email_addr='umairsharif38@gmail.com'
from_email_password='izhar786'
to_email_addr = 'umairsharif138@gmail.com'

#Create Alarm state by default its is off

Alarm_state=False

while True:
    if button.is_pressed:
        Alarm_state=True
        print("Alarm on")



     if Alarm_state==True:
         led.on()
         sleep(1)
         if pir.motion_detected:
             print("Motion Detected")
             led.off()



             #Video Record
             camera.resolution=(600,480)
             camera.rotation=180
             camera.start_recording('alert_video.h264')
             camera.wait_recording(2)
             camera.stop_recording()


             #converting video from .h264 to .mp4
             command= "MP4Box -add alert_video.h264 alert_video.mp4"
             call([command] , shell=True)
             print("video converted")

             #Create the Message
             msg=MIMEMultipart()
             msg['Subject'] = 'INTURDER ALERT ...'
             msg['From'] =from_email_addr
             msg ['To'] = to_email_addr

             #Video Attachment
             Captured='/home/pi/Desktop/alert_video.mp4'#if python Script cannot save on desktop then change the path according to location
             fp=open(Captured, 'rb')
             att=email.mime.application.MIMEApplication(fp.read(),_subtype=".mp4")
             fp.close()
             att.add_header('Content-Disposition' , 'attachment ' , filename='video' + datetime.datetime.now().strftime('%y-%m-d%H%:%M:%S '))
             msg.attach(att)
             print("Attach succesfully")


             #send Mail
             server = smtplib.SMTP('smtp.gmail.com ', 587)
             server.starttls()
             server.login(from_email_addr,from_email_password)
             server.sendmail(from_email_password,to_email_addr,msg.as_string())
             server.quit()
             print('email sent')
             Alarm_state=False

             



             