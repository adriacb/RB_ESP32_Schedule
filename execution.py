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
    fredvic = DDBBConn(ddbbname='rasp_fv22', user='fredvic', passw='Fredvic$21', host='10.31.0.10', pool=3306)



    fredvic.query("drop table if exists data;", debug=True)
    fredvic.query(""" 
    CREATE TABLE data (ID INT NOT NULL AUTO_INCREMENT,
                        Temperatura FLOAT,
                        Humitat FLOAT,
                        Sensacio_termica FLOAT,
                        Corrent FLOAT,
                        Curr_Date TIMESTAMP NOT NULL,
                        PRIMARY KEY (ID)  
                        )
    """, debug=True)



    fredvic.query("""SELECT * FROM data;""", debug=True)
    fredvic.close()


def inserts(temp, hum, sens, curr, date):
    fredvic = DDBBConn(ddbbname='rasp_fv22', user='fredvic', passw='Fredvic$21', host='10.31.0.10', pool=3306)
    fredvic.query("""INSERT INTO data (Temperatura, Humitat, Sensacio_termica, Corrent, Curr_Date) VALUES (%s, %s, %s, %s);""", (temp, hum, sens, curr, date), debug=True)
    fredvic.close()

