#coding=utf-8
import time
import pymysql
import sshtunnel 
import dotenv
import os

def connect_test():
    dotenv.load_dotenv()
    db = pymysql.connect(
        host=os.getenv('TEST_DB_HOST'),
        user=os.getenv('TEST_DB_USER'),
        passwd=os.getenv('TEST_DB_PASSWORD')
    )

    return db,None

def connect_production():
    dotenv.load_dotenv()

    server = sshtunnel.SSHTunnelForwarder(
        ssh_address_or_host=(os.getenv('SSH_HOST'), 22), # 指定ssh登入的跳轉機的address
        ssh_username=os.getenv('SSH_USER'), # 跳轉機的使用者
        ssh_pkey=os.getenv('SSH_PEM_PATH'), # 跳轉機的密碼
        remote_bind_address=(os.getenv('DB_HOST'), 3306)
    )

    server.start()

    db = pymysql.connect(
        host='127.0.0.1',
        port=server.local_bind_port,
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_DATABASE')
    )
    return db,server

def close(db,server):
    db.close()
    if server is not None:
        server.close()