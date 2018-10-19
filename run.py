"""
file to run the end points
"""

from flask import Flask
from api.views.view import Routes

app = Flask(__name__)
app.env = 'development'
Routes.create(app)



if __name__ == '__main__':
    app.run(debug=True)