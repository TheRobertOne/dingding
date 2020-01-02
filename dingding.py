#coding=utf-8
from flask_cors import *
import flask,json
from flask import jsonify
import requests

server = flask.Flask(__name__)
# CORS(server, supports_credentials=True)
class DateEncoder(json.JSONEncoder):
    @server.route('/getAccessToken', methods=['get'])
    @cross_origin()
    def get_access_token():
        headers = {
            'Accept':'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With':'XMLHttpRequest',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
            'Content-Type':'application/json',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Cache-Control':'no-cache',
        }
        data = {}
        data = json.dumps(data)
        url = 'https://oapi.dingtalk.com/gettoken?appkey=dingsqk5c7abvirvjhwv&appsecret=yJRz5O3fP5Y27qOTtexSJfQDC8d59c5CPF0afQoU76L2xcYMAUnmT57FxAIHDjP4'
        response = requests.get(url = url,headers =headers )
        return response.text



server.run(port=7676,host='0.0.0.0')
