# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:29:25 2021

@author: adria.cabello
"""

from MonitorDDBB import DDBBConn
from utils import *
from colorama import Fore, Back, Style
# DDBB
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pymysql





def create_table():
    fredvic = DDBBConn(ddbbname=cred['ddbbname'][0], user=cred['user'][0], passw=cred['pass'][0], host=cred['host'][0], pool=int(cred['pool'][0]) )



    fredvic.query("drop table if exists Sensors_Temp;", debug=True)
    fredvic.query(""" 
    CREATE TABLE Sensors_Temp (ID INT NOT NULL AUTO_INCREMENT,
                    Temperatura_C FLOAT,
                    Temperatura_F FLOAT,
                    Humitat FLOAT,
                    Sensacio_termica_C FLOAT,
                    Sensacio_termica_F FLOAT,
                    Curr_Date TIMESTAMP NOT NULL,
                    Zona VARCHAR(50),
                    PRIMARY KEY (ID)  
                    )
    """, debug=True)



    fredvic.query("drop table if exists Hats;", debug=True)
    fredvic.query(""" 
    CREATE TABLE Hats (ID INT NOT NULL AUTO_INCREMENT,
                        Corrent FLOAT,
                        Tensio FLOAT,
                        Potencia FLOAT,
                        Curr_Date TIMESTAMP NOT NULL,
                        Zona VARCHAR(50),
                        PRIMARY KEY (ID)  
                        )
    """, debug=True)


    fredvic.close()


def inserts(temp, hum, sens, curr, date):
    fredvic = DDBBConn(ddbbname=cred['ddbbname'][0], user=cred['user'][0], passw=cred['pass'][0], host=cred['host'][0], pool=int(cred['pool'][0]) )
    fredvic.query("""INSERT INTO data (Temperatura, Humitat, Sensacio_termica, Corrent, Curr_Date) VALUES (%s, %s, %s, %s);""", (temp, hum, sens, curr, date), debug=True)
    fredvic.close()

