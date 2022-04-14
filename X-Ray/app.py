# required packages 
from flask import Flask,render_template,request,make_response,jsonify
from helper import Helper

helper = Helper()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output/',methods=["POST",'GET']) 
def output():
    bs64string = request.get_json()
    result = helper.predict(bs64string)
    res = make_response(jsonify(result),200)
    return res
    
if __name__ == '__main__':
    app.run(debug=True)
