from flask import Flask, jsonify
import flask
import chat

app = Flask(__name__)

@app.route("/",methods=["POST"])
def hello_world():
    json_data = flask.request.json
    return jsonify(str(chat.getResposta(json_data["pergunta"]))) #melhorar