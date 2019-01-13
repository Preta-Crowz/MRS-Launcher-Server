# -*- coding: utf-8 -*-
import base64
import json
from datetime import *
import flask
import requests
from flask import Flask, Response, make_response
from flask_restful import Api, Resource, reqparse

APP = Flask(__name__)
API = Api(APP)

'''class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=9) + self.dst(dt)

    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime(dt.year, 4, 1)   # ends last Sunday in October
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() + 1)
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=9)
        else:
            return timedelta(0)

    def tzname(self, dt):
        return "GMT +19"'''




class list(Resource):
    def get(self):
        with open("list.json", "r") as f:
            res = f.read()
        res=make_response(res)
        res.headers['Content-Type'] = "application/json; charset=utf-8"
        return res


API.add_resource(list, '/modpack')
if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
