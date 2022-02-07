import os
from datetime import datetime

# DDBB
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pymysql

# Pandas (dataframes)
import pandas as pd
from pandas.core.frame import DataFrame
from pandas.io.sql import read_sql

# Terminal styling
from colorama import Fore, Back, Style

class DDBBConn:
    """
    Description: class DDBConn
    
    This class allows the connection 
    
    
    Parameters
    ----------
    ddbbname: str 
        - Database name
    user: str     
        - Username
    passw: str    
        - Password

        
    Example
    -------
    >>> myDB = DDBBConn(ddbbname='dbname', user='root', passw='1234', host='127.0.0.1')
    >>> myDB.query("drop table if exists MyTable;", debug=True)
    >>> df = myDB.query("
                        select * from MyTable
                        ", debug=False)
    >>> df.head() # returns a pd.DataFrame if the query is "Select"
    """
    
    def __init__(self, ddbbname: str, user: str, passw: str, host: str, pool: int = 3600):
        """
        TO DO: encapsulate variables
        """
        self.ddbbname = ddbbname
        self.user = user
        self.passw = passw
        self.host = host
        self.status = "Correct"
        self.pool = pool
            
        try:
            print(f'mysql+pymysql://{self.user}:{self.passw}@{self.host}/{self.ddbbname}')
            self.sqlEngine = create_engine(f'mysql+pymysql://{self.user}:{self.passw}@{self.host}/{self.ddbbname}', pool_recycle=self.pool) #3600
            self.dbConnection = self.sqlEngine.connect()
            print(Back.GREEN + "Successful connection."+Style.RESET_ALL)
           
        except:
            print(Back.RED + "Refused connection."+Style.RESET_ALL)

        self.date = datetime.now()

      
    
    def query(self, querySQL:str, debug: bool = True) -> pd.DataFrame:
        """
        Description
        ----------------------------------------
        Function that generates a query, if there is an error we want to store
        that error in a log file, this log file is generated each time that the
        script is runned, we will generate a folder for each day, and since this 
        script will be executed 8 times in a day, we will have 8 
        self.date.strftime('%m').log files for day. 
        
        In case of Exception or error, if debug=False, we can send a notification
        via eMail. TO DO
        
        Parameters
        ----------
        querySQL: str
            It is basically the SQL query we want to perform.
            
        Precondition
        ------------
            if the query is select and it is possible.
        
        Returns
        -------
        pd.DataFrame
            - It contains the result of the SELECT query.
        """
        
        startTime = datetime.now()

        # by default frame = empty
        frame = pd.DataFrame()
        
        try:
            
            if querySQL.lower().startswith('select'):
                frame = pd.read_sql(querySQL, self.dbConnection)  
                        
            else:
                try:
                    self.dbConnection.execute(text(querySQL))
                except Exception as e:
                    print(e)
                    self.status = e
                
            endTime = datetime.now()
            timeSpent = endTime - startTime

            print(Back.GREEN +f"Has been completed in {timeSpent}."+Style.RESET_ALL)
             
            

        except Exception as e:
            endTime = datetime.now()
            timeSpent = endTime - startTime            

              
            print(e.args)
            print(e)
            self.status = e
        
        return frame, self.status
            
            
    def close(self):
        self.dbConnection.close()