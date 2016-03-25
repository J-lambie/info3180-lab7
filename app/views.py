from flask import Flask, abort, request, jsonify, g, url_for, render_template
import requests
from image_getter import image_dem

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm home"

@app.route('/thumbnails', methods=['GET','POST'])
def thumbnails():
    if request.method == 'POST' :
        url=request.form['url']
        r=requests.get(url)
        if r.status_code==200:
            thumbnails=image_dem(url)
            obj={'error': 'null','data':{'Thumbnail':thumbnails},'message':'success'}
            json=jsonify(obj)
            #Remove the comment below to return Json and comment the return render_template
            #return json
            return render_template('view.html',thumbnails=thumbnails)
        json=jsonify({'error':"1",'data':{},'message':'failure'})
        #Remove the comment below to return Json and comment the return render_template
        #return json
        return render_template('view.html')
    else:
        return render_template('form.html')    
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)