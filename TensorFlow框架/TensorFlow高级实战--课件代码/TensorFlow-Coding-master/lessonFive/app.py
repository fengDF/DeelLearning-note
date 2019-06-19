
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import tensorflow as tf
import os
from flask import Flask, render_template, request, make_response
from flask import jsonify
from flask import Flask
from flask import jsonify
from flask import Response
import sys
import time  
import hashlib
import threading
import execute
import random


import getConfig

gConfig={}

gConfig=getConfig.get_config(config_file='config.ini')

COLUMNS1 = [ '1','2',  '3',  '4',  '5',  '6',  '7',  '8',  '9',  '10', '11', '12', '13', '14', '15', '16', '29', '30', '31']
#test_set = pd.read_csv(gConfig['test_set'], skipinitialspace=True,skiprows=1, names=COLUMNS1)
app = Flask(__name__) 
#路由注解，我们这里使用的是path的形式进行传参
#
@app.route('/predict',methods=['GET'])
	#/<a>/<b>/<c>/<d>/<e>/<f>/<g>/<h>/<i>/<j>/<k>/<l>/<m>/<n>/<o>/<p>/<q>/<r>', methods=['GET'])
#@app.route('/predict/<a>/<b>/<c>/<d>', methods=['GET'])
def predict():
	#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
	#获取url传来的需要进行预测的数据
	   result_k=[]
	   result_line=[]
	   data=[[0,1.57,0,0,1.58,0,0,99.92,0,0,99.92,0,477.79,348.23,6.24,0,12.4545,-5.2992],
	      [0,1.23,0,0,1.31,0,0,99.92,0,0,99.92,0,475.82,348.45,6.19,0,-0.3895,0.576],
	      [60.57,60.49,60.5,60.5,60.49,60.49,99.9,99.86,99.9,99.9,99.86,99.9,453.07,351.83,6.07,111.4,-1.254,1.536]]
	#for l in range(3):
	   l=random.randint(0,2)
	   line=data[l]
	#line=[a,b,c,d]
	   lines=range(3)
	   lines=[float(i) for i in line]
	   line_train=[]
	   line_train.append(lines[-2])
	   line_train.append(lines[-1])
	#因为我们全量的数据是31列，所以我们要在数据后面增加一个元素
	   line_train.append(0)
	   COLUMNS = [ '29', '30', '31']

	#将数组转换成dataframe[[1,2,3]]

	   lines= pd.DataFrame([line_train],columns=COLUMNS)
	
	#predict_result=train.predict(lines)
	   predict_result=execute.predict(sess,lines,model)
	   if predict_result[0]==0:
	   	  k="正常"
	   	  key=0
	   else:
	   	  k="有漏油"
	   	  key=1
	   result_k.append(k)
	   result_line.append(line)

	   return render_template('predict.html',result_k=result_k,result_line=result_line,key=key)
#初始化session，大家想一下如果不初始化会有什么问题？
sess = tf.Session()
sess, model = execute.init_session(sess, conf='config.ini')

if (__name__ == "__main__"): 
    app.run(host = '0.0.0.0', port = 8088) 


