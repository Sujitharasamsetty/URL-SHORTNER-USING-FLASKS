from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

data = {}

############################3
@app.route('/')
def home_get():
    return render_template('home.html')

@app.route('/', methods=['POST'])

def home_post():
    original_url = request.form.get('in_1')
    short_url = random.randint(1, 100)
    data[short_url] = original_url
    return render_template('home.html')

@app.route('/history')
def history_get():
    return render_template('history.html', data=data)

@app.route('/sh/<short>')
def fun(short):
    if int(short) in data:
        return "Redirect to {}".format(data[int(short)])
    return "incorrect URL"

##############################


if __name__ == "__main__":
    app.run(debug=True)