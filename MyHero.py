from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'My Hero!!!'


if __name__ == '__main__':
    app.run(port='80')
