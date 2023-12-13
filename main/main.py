from flask import Flask
app = Flask(__name__)
app.secret_key = 'your_secret_key' 

from core import routes

if __name__ == '__main__':
    app.run(debug=True)