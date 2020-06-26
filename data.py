import pandas as pd 
from newsapi import NewsApiClient
import requests
import tensorflow_datasets as tfds

res = requests.get("http://pplapi.com/random/json").json()
print(res)

dataset, info = tfds.load('scientific_papers',with_info=True)

