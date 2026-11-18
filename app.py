# web app

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    q = request.form.get('q')
    return (render_template('index.html'))

@app.route('/main', methods=['GET', 'POST'])
def main():
    return (render_template('main.html'))

if __name__ == '__main__':
    app.run()