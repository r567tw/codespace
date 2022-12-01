#coding=utf-8
import json
import os
import urllib

import boto3
import dotenv
import pymysql
import requests
from botocore.exceptions import ClientError

from helpers import MySqlHelper

# 連線資料庫
dotenv.load_dotenv('.env')
env = os.getenv('ENV')
print("目前環境:{}".format(env))

if env == 'production':
    print("連線到正式資料庫")
    connection,server =  MySqlHelper.connect_production()
else:
    print("連線到測試資料庫")
    connection,server =  MySqlHelper.connect_test()
cursor = connection.cursor(pymysql.cursors.DictCursor)
# 連線資料庫結束

# SQL語法
sql = "select id,imgCover from ear.channels where imgCover is not null"
# 執行語法
cursor.execute(sql)
#獲得結果
results = cursor.fetchall()
# result = cursor.fetchone()

# 打開檔案紀錄
logs = open('log','w')

for result in results:
    # code here
    logs.write(result)    

logs.close()

# 關閉連線
MySqlHelper.close(connection,server)
print('完成!')
