import requests

from flask import Flask, render_template

base_url = 'http://192.168.0.112/api/SGpkOeCn3JCOpW-YqAyE-cFIk7U3w59SKrDCm89G'
app = Flask(__name__)

def get(endpoint):
    return requests.get(base_url + endpoint).json()

def put(endpoint, json):
    return requests.put(base_url + endpoint, json=json).json()[0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle/', methods=['PUT'])
def toggle():
    response = get('/lights')
    hue = response['2']['state']['hue']
    response = put('/lights/2/state', {'hue': 46920 if hue == 8906 else 8906})
    print(response)
    print(type(response))
    return response

if __name__ == '__main__':
    app.run(port=8888, debug=True) 