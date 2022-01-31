from flask import Flask, request, jsonify

# Application
app = Flask(__name__)

# Configuration Dictionary
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQL_TRACK_MODIFICATIONS"] = 0