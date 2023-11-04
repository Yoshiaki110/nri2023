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


import make_qrcode
import connect_qr

SPOTFILE = './static/spot.json'
BUYEDFILE = './buyed.json'
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

# 所有カードのページ
@app.route('/cards')
def cards():
  print("** /cards " + request.method)
  title = '御朱印OTAKU'
  with open(BUYEDFILE, "r", encoding="utf-8") as f:
    buyed = json.load(f)
  resp = make_response(render_template("cards.html", title=title, buyed=buyed))
  return resp

# ログインページ
@app.route('/login')
def login():
  print("** /login " + request.method)
  title = '御朱印OTAKU'
  resp = make_response(render_template("login.html", title=title))
  return resp

# 印刷中ページ
@app.route('/printed')
def logprintedin():
  print("** /printed " + request.method)
  title = '御朱印OTAKU'
  resp = make_response(render_template("printed.html", title=title))
  return resp

# ダウンロード
@app.route('/download', methods=["GET", "DELETE"])
def download():
  print("** /download " + request.method)
  path = './static/res/res.jpg'
  if request.method == "GET":
    if os.path.exists(path):
      return send_file(path, as_attachment=True)
    else:
      return jsonify({'message': 'hello internal'}), 404
  if request.method == "DELETE":
    os.remove(path)
    return '200'

# カードを印刷するAPI
@app.route('/prt/<id>', methods=["PUT"] ) 
def prt(id):
  print("** /prt/" + id + " " + request.method)
  # 購入データの更新
  with open(BUYEDFILE, "r", encoding="utf-8") as f:
    buyed = json.load(f)
  now = datetime.datetime.now()
  dt = {
    "date": now.strftime('%Y/%m/%d'),
    "hash": "xxxxx",
    "id": id
  }
  buyed.append(dt)
  with open(BUYEDFILE, "w", encoding="utf-8") as f:
    json.dump(buyed, f, indent=2)
  '''
  ここに印刷の処理入れてください
  idは、５桁の文字型の数字にします（例、12345）。
  ./static/img ディレクトリに画像ファイルがあります
  画像ファイルは、id.jpg（例、12345.jpg）
  QRコードは、http://localhost:5000/spot/id に飛ぶようにしてください
  '''
  qr_img = make_qrcode.make_qrcode(id)
  connect_qr.connect_qr(qr_img, id)

  return '200'


if __name__ == '__main__':
  app.run(debug=True)
