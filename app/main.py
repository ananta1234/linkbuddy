from flask import Flask, render_template, request
# import pyshorteners
import pandas as pd


app = Flask(__name__)


def shorten_url(long_url):
  # s = pyshorteners.Shortener()
  # short = s.tinyurl.short(long_url)
  short = long_url[:5]
  return short

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      mess = result["message"]
      urls = mess.split("\n")

      short_urls = []

      for u in urls:
        u = u.strip()
        sh = shorten_url(u)
        short_urls.append(sh)

      return render_template("result.html",result = short_urls)