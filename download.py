# -*- coding: utf-8 -*-

import requests

url='http://localhost:5000'
res = requests.get(url + '/download')
if res.status_code < 200 or res.status_code >= 300:
  print('error')
  pass
urlData = res.content
with open('tmp.jpg' ,mode='wb') as f: # wb でバイト型を書き込める
  f.write(urlData)

requests.delete(url + '/download')
