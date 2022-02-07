# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:20:05 2021

@author: adria.cabello
"""

#conda install -c conda-forge schedule

import schedule
import time
from MonitorDDBB import DDBBConn
from utils import *
from execution import inserts
from datetime import timedelta
import pandas as pd

csv_path = '/home/pi/DADES_ZONA2.csv'


test_csv = "test.csv"

def insert_csv(path):

    df = pd.read_csv(path, names=['Temperatura', 'Humitat', 'Sensacio_termica', 'Corrent', 'Curr_Date'])

    fredvic = DDBBConn(ddbbname='rasp_fv22', user='fredvic', passw='Fredvic$21', host='10.31.0.10', pool=3306)
    
    df.to_sql(name='data', con=fredvic.dbConnection, if_exists='append', index=False) # append

    fredvic.close()


def test():
    schedule.clear()
    
    #inserts()
    #time.sleep(2)
    #checkNullsAccions()    

def main():
    schedule.every(15).minutes.do(insert_csv, path=test_csv)
    # # # schedule.every(8).hours.do(inserts)
    # # # # schedule.every(20).seconds.do(checkNullsAccions)
    
    while True:
        print(f"{datetime.now()} ")
        schedule.run_pending()
        time.sleep(1) 

if __name__ == '__main__':
    #test()
    main()

    