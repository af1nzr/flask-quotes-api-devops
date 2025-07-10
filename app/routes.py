from flask import Blueprint, jsonify
from .quotes import get_random_quote

api = Blueprint('api', __name__)

@api.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Quotes API"})

@api.route("/quote", methods=["GET"])
def quote():
    return jsonify({"quote": get_random_quote()})
