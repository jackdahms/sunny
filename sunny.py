import requests

from flask import Flask, render_template

from kivy.app import App
from kivy.uix.button import Button

base_url = 'http://192.168.0.112/api/SGpkOeCn3JCOpW-YqAyE-cFIk7U3w59SKrDCm89G'
app = Flask(__name__)

def get(endpoint):
    return requests.get(base_url + endpoint).json()

def put(endpoint, json):
    return requests.put(base_url + endpoint, json=json).json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle/')
def toggle():
    response = get('/lights')
    hue = response['2']['state']['hue']
    put('/lights/2/state', {'hue': 46920 if hue == 8906 else 8906})

class TestApp(App):
    def build(self):
        toggle = Button(text='Toggle Lights')
        toggle.bind(on_press=self.toggle_lights)

        return toggle

    def toggle_lights(self, instance):
        response = get('/lights')
        hue = response['2']['state']['hue']
        print(hue)
        response = put('/lights/2/state', {'hue': 46920 if hue == 8906 else 8906})
        print(response)

if __name__ == '__main__':
    # app.run(debug=True)
    TestApp().run()