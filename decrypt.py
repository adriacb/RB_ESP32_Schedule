import os
import pandas as pd
import cryptpandas as crp


def encrypt(path):
    df = pd.read_csv(path, names=['ddbbname','user', 'pass', 'host', 'pool'])
    crp.to_encrypted(df, password='Fredvic$22', path='file.crypt')

def decrypt():
    decrypted_df = crp.read_encrypted('file.crypt', password='Fredvic$22')
    return decrypted_df



if __name__ == "__main__":
    encrypt(os.getcwd()+'\credentials.csv')
