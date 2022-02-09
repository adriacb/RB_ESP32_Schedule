# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 08:15:06 2021

@author: adria.cabello
"""
import os


from datetime import datetime

# SEND MAIL
import ssl
import smtplib
from smtplib import SMTP
from getpass import getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage


# Terminal styling
from colorama import Fore, Back, Style


def send_mail(msg: list, status, sender: str='adria.cabello@', password: str='', receiver:str ='adrian.cabello@'):
    
    if status == 'Correct':
        print(Back.GREEN +f"STATUS {status}"+Style.RESET_ALL)
    else:
        print(Back.RED +f"STATUS {status}"+Style.RESET_ALL)
    
    try:
        message = MIMEMultipart("alternative")
        message['Subject'] = msg[0]
        message['From'] = sender
        message['To'] = receiver
        #part1= MIMEText(msg[1], "plain")
        part2= MIMEText("".join(msg[1:]), "html")
        #message.attach(part1)
        message.attach(part2)
        
        with SMTP("smtp.office365.com", port=587) as s:
            sslcontext = ssl.create_default_context()
            s.starttls(context=sslcontext)
            s.login(sender, password)
            s.sendmail(sender, receiver, message.as_string())
    except Exception as e:
        print(e)
        print(e.args)
        #return e



def checkDir(dir: str):
    if not os.path.exists(dir):
        print(Back.RED +dir+ " does not exists, creating this directory..."+Style.RESET_ALL)
        os.mkdir(dir)
    else:
        print(Fore.GREEN+ dir+ " already exists."+Style.RESET_ALL)


def checkFile(file: str):
    if not os.path.exists(file):
        print(Back.RED +file+ " does not exists, creating this file..."+Style.RESET_ALL)
        f = open(file, "a+")
        f.close()
    else:
        print(Fore.GREEN+file+" already exists."+Style.RESET_ALL)
        

def checkDirs(rootName: str):
    
    """
    The names of the paths that we are going to create.
    
    basePath ddbbname~YYYY
        |
        pathMonth /MM
        |    |
        |    pathDay /DD
        |    |    |
        |    |    file.log
        
    
    >>> rootName=Peticions
   
    """
    if not os.path.exists('logs'):
        os.mkdir('logs')
    else:
        print(Fore.GREEN+"logs already exists."+Style.RESET_ALL)
    dirs = {
        'basePath': f"logs/{rootName}~{datetime.now().year}",
        'pathMonth': os.path.join(f"logs/{rootName}~{datetime.now().year}", f"{datetime.now().date().strftime('%m')}"),
        'pathDay': os.path.join(os.path.join(f"logs/{rootName}~{datetime.now().year}", f"{datetime.now().date().strftime('%m')}"), f"{datetime.now().date().day}"),
        'file': os.path.join(os.path.join(os.path.join(f"logs/{rootName}~{datetime.now().year}", f"{datetime.now().date().strftime('%m')}"), f"{datetime.now().date().day}"), f"{datetime.now().now().strftime('%H.%M.%S')}.html"),
        'updated_file': os.path.join(os.path.join(os.path.join(f"logs/{rootName}~{datetime.now().year}", f"{datetime.now().date().strftime('%m')}"), f"{datetime.now().date().day}"), f"updated_{datetime.now().now().strftime('%H.%M.%S')}.html")            
        }

    for p in dirs:
        if p != 'file' and  p != 'updated_file':
            checkDir(dirs[p])
        else:
            checkFile(dirs[p])
        
    return dirs


import cryptpandas as crp

def decrypt():
    decrypted_df = crp.read_encrypted('file.crypt', password='Fredvic$22')
    return decrypted_df


cred = decrypt()
#print(cred)