import requests

from flask import Flask, render_template, current_app, url_for

base_url = 'http://192.168.0.112/api/SGpkOeCn3JCOpW-YqAyE-cFIk7U3w59SKrDCm89G'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/poll')
def is_group_on():
    response = requests.get(base_url + '/groups').json()
    return response['1']['state']

@app.route('/toggle', methods=['PUT'])
def toggle():
    new_state = not is_group_on()['all_on']
    json = {'on': new_state}
    response = requests.put(base_url + '/groups/1/action', json=json)
    return response.json()[0]

if __name__ == '__main__':
    app.run(port=8888, debug=True) 