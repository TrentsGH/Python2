import os
import tarfile
import urllib.request as request
#import pandas as pd

DOWNLOAD_ROOT = 'https//raw.githubusercontent.com/ageron/handson-m12/master/'
HOUSING_PATH = os.path.join('datasets','housing')
HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.tgz'

def fetch_data(housing_url=HOUSING_URL,housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    tar_path = os.path.join(housing_path,'housing.tgz')
    request(housing_url,tar_path)
    housing_tgz = tarfile.open(tar_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

fetch_data()
'''
def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, 'housing.csv')
    return pd.read_csv(csv_path)

#housing = load_housing_data()
#housing.head()
'''