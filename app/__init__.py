# Initialize the our package 'app' 
from flask import Flask

app = Flask(__name__)
from app import views