from image_getter import image_dem
from _init_ import db, app
import models,requests
from flask import Flask, abort, request, jsonify, g, url_for

@app.route('/thumbnails/<str:url>')
def get_thumbnails(url):
    r=requests.get(url)
    if r.status_code==200:
        thumbnails=image_dem(url)
        return jsonify({'error': 'null','data':{'Thumbnail':thumbnails},'message':'success'})
    return jsonify({'error':"1",'data':{},'message':'failure'})
        
    

