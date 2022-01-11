from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/hire', methods = ['GET'])
def hire():
    return render_template('hire.html')

@app.route('/about', methods = ['GET'] )
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)