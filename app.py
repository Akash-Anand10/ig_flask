from flask import Flask, request, redirect, url_for, render_template
from API.data import extract

app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    # return '''<html><body><h1>Welcome to Instagram Media Comments Extractor!!</h1>
    # <p>For now, we have to pass the media url as parameters.
    # Please type in the Media url as parameter in the URL bar and press enter.</p></body></html>'''
    return render_template('comments.html')

@app.route('/comments/', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        url = request.form['url']
        return f'''{extract(url)}'''
    else:
        url = request.args.get('url')
        return f'''{extract(url)}'''

@app.route('/form/', methods=['GET'])
def form():
    return render_template('comments.html')