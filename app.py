from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    if request.method == "POST":
        print(request_form)
        props = {}
        return render_template('results.html', props = props)
    else:
        return render_template('results.html')