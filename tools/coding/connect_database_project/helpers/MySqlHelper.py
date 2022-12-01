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

def insertEpisodeMapping(connection,channelId,episodeId):
    cursor = connection.cursor()
    cursor.execute('insert into ear.episode_mapping(collaboration_id,collaboration_episode_id) values (%s,%s)',(channelId,episodeId))
    connection.commit()

def existChannelMapping(cursor,id):
    cursor.execute('SELECT * FROM ear.channel_mapping WHERE collaboration_id=%s and channel_id is not null', (id))
    mapping = cursor.fetchall()
    return len(mapping) >= 1

def existEpisodeMapping(cursor,id):
    cursor.execute('SELECT * FROM ear.episode_mapping WHERE collaboration_episode_id=%s', (id))
    mapping = cursor.fetchall()
    return len(mapping) >= 1

def getOurChannelId(cursor,id):
    cursor.execute('SELECT * FROM ear.channel_mapping WHERE collaboration_id=%s', (id))
    mapping = cursor.fetchone()
    return mapping[9]

def getEpisodesData(cursor):
    cursor.execute('SELECT id as episodeId,url from ear.episodes where channel_id in (select channel_id from ear.channel_mapping where channel_id is not null) and status=0 order by id desc')
    episodes = cursor.fetchall()
    return episodes