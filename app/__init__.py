from flask import Flask

app = Flask(__name__)
app.secret_key = "H*(QW&Es9d8fu38(*W"
from app import views