# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:29:28 2020

@author: Syed
"""

from flask import Flask, jsonify, request
#from LDML import ldm
from NaiveLDML import ldm
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return "Server is working"
#  

@app.route("/ldml/<int:age>/<int:headsize>/<int:fits>/<int:hyg>/<int:motor>/<int:grossmot>/<int:express>/<int:iqob>/<int:iqtime>/<int:iqface>/<int:sim>/<int:simtime>/<int:simface>/<int:arith>/<int:arithtime>/<int:arithface>/<int:shape>/<int:shapetime>/<int:shapeface>/<int:col>/<int:coltime>/<int:colface>/<int:read>/<int:readtime>/")
def ld(age, headsize, fits, hyg, motor, grossmot, express, iqob, iqtime, iqface, sim, simtime, simface, arith, arithtime, arithface, shape, shapetime, shapeface, col, coltime, colface, read, readtime):
    tester = { 'Age': [age],
        'HeadSize': [headsize],
        'fits' :[fits],
        'Personal_hygiene' :[hyg],
        'fine motor skills' :[motor],
        'gross motor skills' :[grossmot],
        'expressive skills' :[express],
        'IQ Obatained Score' :[iqob],
        'IQ Time' :[iqtime],
        'IQ FaceTime' :[iqface],
        'Similarity Score' :[sim],
        'Similarity time' :[simtime],
        'Similarity facetime' :[simface],
        'ArthmeticScore' :[arith],
        'ArthmeticTime' :[arithtime],
        'Arthmetic Facetime' :[arithface],
        'ShapeTest Score' :[shape],
        'ShapeTest Time' :[shapetime],
        'ShapeTest Facetime' :[shapeface],
        'ColorTest Score' :[col],
        'ColorTest Time' :[coltime],
        'ColorTest Facetime' :[colface],
        'Reading Score' :[read],
        'Reading Time' :[readtime]
        }
    df = pd.DataFrame(tester, columns = ['Age', 'HeadSize','fits', 'Personal_hygiene', 'fine motor skills', 'gross motor skills', 'expressive skills', 'IQ Obatained Score', 'IQ Time', 'IQ FaceTime','Similarity Score', 'Similarity time', 'Similarity facetime', 'ArthmeticScore', 'ArthmeticTime', 'Arthmetic Facetime', 'ShapeTest Score', 'ShapeTest Time', 'ShapeTest Facetime', 'ColorTest Score', 'ColorTest Time', 'ColorTest Facetime','Reading Score', 'Reading Time'])
    answer = ldm(df)
    answer = int(answer)
    return jsonify({"answer":answer})

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
