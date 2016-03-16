import json
import os
import pandas as pd
import requests

root = os.environ['HOME']
folder = os.path.join(root,'projects','weatherdata')
key_path = os.path.join(folder, 'key.txt')


date = pd.datetime.now().strftime('%Y-%m-%d')
file_name = date + '_allsites.json'
file_path = os.path.join(folder,'json_files',file_name)

with open(key_path, 'r') as f:
	key = json.load(f)['key']

url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/all?res=hourly&key='

req = requests.get(url+key)

with open(file_path, 'wb') as f:
	for chunk in req.iter_content(100000):
		f.write(chunk)
