# -*- coding: utf-8 -*-

import os
from flask import Flask, redirect, render_template, request, jsonify, make_response, send_file
import base64
import uuid
import socket
from io import BytesIO
import datetime
import json
import ftplib

SPOTFILE = './static/spot.json'
app = Flask(__name__)
spots = {}

# 地図のページ
@app.route('/')
def index():
  print("** / " + request.method)
  title = '御朱印OTAKU'
  resp = make_response(render_template("index.html", title=title))
  return resp

# 各スポットのページ
@app.route('/spot/<id>') 
def spot(id):
  global spots
  print("** /spot/" + id + " " + request.method)
  with open(SPOTFILE, "r", encoding="utf-8") as f:
    spots = json.load(f)
  s = [s for s in spots if s['id'] == id][0]
  title = '御朱印OTAKU'
  memo = s['memo']
  name = s['name']
  resp = make_response(render_template("spot.html", title=title, id=id, name=name, memo=memo))
  return resp

# カードを印刷するAPI
@app.route('/prt/<id>', methods=["PUT"] ) 
def prt(id):
  print("** /prt/" + id + " " + request.method)
  '''
  ここに印刷の処理入れてください
  idは、５桁の文字型の数字にします（例、12345）。
  ./static/img ディレクトリに画像ファイルがあります
  画像ファイルは、id.jpg（例、12345.jpg）
  QRコードは、http://localhost:5000/spot/id に飛ぶようにしてください
  '''
  return '200'


if __name__ == '__main__':
    app.run(debug=True)
