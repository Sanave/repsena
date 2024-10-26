from flask import Flask, render_template;

flask = Flask(__name__)

if __name__ == '__main__':
    flask.run(debug=True)

@flask.route('/')
def index():
    return render_template('index.html')

@flask.route('/otro')
def segunda():
    return render_template('otro.html')
