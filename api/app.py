from flask import Flask
from .vr_1.views import Routes

app = Flask(__name__)
Routes.create(app)
app.env = 'development'