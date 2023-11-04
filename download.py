# -*- coding: utf-8 -*-

import time
import requests

def get():
  url = 'http://localhost:5000'
  #url = 'https://lwbr9qf6-5000.asse.devtunnels.ms'
  res = requests.get(url + '/download')
  if res.status_code < 200 or res.status_code >= 300:
    print('no file')
    return
  urlData = res.content
  with open('tmp.jpg' ,mode='wb') as f: # wb でバイト型を書き込める
    f.write(urlData)
  print('download done')

  requests.delete(url + '/download')
  print('delete print file')

while True:
  get()
  time.sleep(5)