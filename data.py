import pandas as pd 
from newsapi import NewsApiClient
import requests

res = requests.get("http://pplapi.com/random/json").json()
print(res)