from datetime import datetime, timedelta
import time
import random
import time
import requests
import json
import urllib.request

def print_numbers(url):
  r = requests.get(url)

  pak_json = r.json()
  list = [] 
  random_num  = random.randint(0,25)
  pakg_str = json.dumps(pak_json[random_num]['download_url'])
  ss = pakg_str.replace('"','')
  list.insert(0,ss)
  ss = [random.choice('0123456789') for _ in range(1,5)]
  ss2 = "".join(ss)  
  Image1  = urllib.request.urlretrieve(list[0],f'Imagee{ss2}.jpg')
  print(ss2, ' : ',list[0])
  print('-------END--------')
  # brust=True
  return  True


  