# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:20:05 2021

@author: adria.cabello
"""

#conda install -c conda-forge schedule
import os
import schedule
import time
from MonitorDDBB import DDBBConn
from utils import *
from execution import inserts, create_table
from datetime import timedelta
import pandas as pd

csv_path_temps = '/home/pi/DADES_ZONA2.csv'
test_csv_hats = "test.csv"

def insert_csv_temp(path):

    df = pd.read_csv(path, names=['Temperatura_C','Temperatura_F', 'Humitat', 'Sensacio_termica_C', 'Sensacio_termica_F', 'Curr_Date', 'Zona'])

    fredvic = DDBBConn(ddbbname=cred['ddbbname'][0], user=cred['user'][0], passw=cred['pass'][0], host=cred['host'][0], pool=int(cred['pool'][0]) )
    
    df.to_sql(name='Sensors_Temp', con=fredvic.dbConnection, if_exists='append', index=False) # append

    fredvic.close()

    # potser borrem l'arxiu un cop s'ha inserit?

    os.remove(path)


def insert_csv_hats(path):
    
    df = pd.read_csv(path, names=['Corrent','Tensio', 'Potencia', 'Curr_Date', 'Zona'])

    fredvic = DDBBConn(ddbbname=cred['ddbbname'][0], user=cred['user'][0], passw=cred['pass'][0], host=cred['host'][0], pool=int(cred['pool'][0]) )
    
    df.to_sql(name='Hats', con=fredvic.dbConnection, if_exists='append', index=False) # append

    fredvic.close()

    # potser borrem l'arxiu un cop s'ha inserit?

    os.remove(path)


def clear_table():
    schedule.clear()
    create_table()

def test_conn(cd):
    schedule.clear()
    fredvic = DDBBConn(ddbbname=cd['ddbbname'][0], user=cd['user'][0], passw=cd['pass'][0], host=cd['host'][0], pool=int(cd['pool'][0]) )
    fredvic.close()



def main():
    schedule.every(5).minutes.do(insert_csv_temp, path=csv_path_temps)
    time.sleep(1) # wait for the first execution
    #schedule.every(5).minutes.do(insert_csv_hats, path=test_csv_hats)

    #.hours.do, .days.do, .minutes.do, .seconds.do

    
    while True:
        print(f"{datetime.now()} ")
        schedule.run_pending()
        time.sleep(1) 

if __name__ == '__main__':
    print(cred)
    #test_conn(cred)
    # schedule.clear()
    main()

    