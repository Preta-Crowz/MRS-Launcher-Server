# -*- coding: utf-8 -*-

import json
config = json.load(open("config.json"))

# import zerologger as zlog
# logger = zlog.Logger(config["RAVEN"]["KEY"],config["RAVEN"]["SECRET"],config["RAVEN"]["PROJECT"],config["APPNAME"],config["LOG"])

from flask import Flask,render_template,request,send_file
# logger.debug("flask imported")
'''
try:
    from winmagic import magic
except:
    import magic
logger.debug("magic imported")
import time
logger.debug("time imported")
import re
logger.debug("re imported")
import requests
logger.debug("requests imported")
'''
# logger.info("Setting up application")
app = Flask(config["APPNAME"])
'''
import logging
logging.getLogger('werkzeug').setLevel(-100)
logger.debug("Flask logging disabled")
'''


@app.route('/modpack')
def mplist():
    return response(open('list.json').read())



def ip(): # Based on openNAMU ip_check
    xff = ""
    try:
        temp = request.headers.getlist("X-Forwarded-For")[0]
        temp = temp.split(":") [:-1]
        for t in temp:
            xff += ":" + t
        xff = xff[1:]
        ip = request.environ.get('HTTP_X_REAL_IP', xff)
    except:
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    # if str(ip) == str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr)) or str(ip) == '::1':
    #     ip = 'Reverse Proxy or Local'
    return str(ip)



def response(res):
    '''rurl = request.url.replace("http://mrs.mc-srv.com:10000","")
    if request.method == "GET":
        logger.info("{} got {}".format(ip(),rurl))
    elif request.method == "POST":
        logger.info("{} posted {}".format(ip(),rurl))
    else:
        logger.info("{} accessed {} with {} request".format(ip(),rurl,request.method))
    if request.cookies:
        logger.debug("Cookies : {}".format(request.cookies))
    if request.data:
        logger.debug("Data : {}".format(request.data))
    if request.form:
        logger.debug("Form : {}".format(request.form))
    if request.json:
        logger.debug("Json : {}".format(request.json))
    if request.headers:
        logger.debug("Headers : {}".format(request.json))
    logger.debug("UA : {}".format(request.user_agent))'''
    if type(res) == dict:
        return json.dumps(res, ensure_ascii=False).encode().decode('utf8')
    elif type(res) == str:
        return res.encode().decode('utf8')

def loop():
    # logger.info("Starting up..")
    try:
        app.run(host=config['HOST'],port=config['PORT'])
    except:
        # logger.exception("Server crashed!")
        # logger.info("Restarting server..")
        loop()
loop()