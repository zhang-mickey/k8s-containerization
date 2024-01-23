# import numpy as np
# import requests
# import ast
# import time
# from threading import Lock, Thread
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
# from kafka import KafkaConsumer
# import redis
#Python 3.9.7
#Flask 1.1.2

#eventlet==0.35.0

#Flask-SocketIO==5.3.6
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

# thread = None
# thread_lock = Lock()
# # 配置项目
# time_interval = 1
# kafka_bootstrap_servers = "10.0.0.222:9092"
# redis_con_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)

# 页面路由与对应页面的ws接口
# 系统时间
# @socketio.on('connect', namespace='/sys_time')
# def sys_time():
#     def loop():
#         while True:
#             socketio.sleep(time_interval)
#             current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())#获取系统时间
#             socketio.emit('sys_time',
#                           {'data': current_time},
#                           namespace='/sys_time')
#
#     socketio.start_background_task(target=loop)


# 欢迎页面
@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html', async_mode=socketio.async_mode)

@app.route('/outline')
def outline():
    return render_template("outline.html", async_mode=socketio.async_mode)

@app.route('/id')
def id():
    return render_template("id.html", async_mode=socketio.async_mode)


# 实时日志分析页面
@app.route('/analysis')
def analysis():
    return render_template('analysis.html', async_mode=socketio.async_mode)


@app.route('/about')
def about():
    return render_template("about.html", async_mode=socketio.async_mode)

@app.route('/index')
def index():
    return render_template("index.html",
                           async_mode=socketio.async_mode
                           )


if __name__ == '__main__':
    socketio.run(app,
                 # host="0.0.0.0",
                 # port=5000,
                 debug=True)



