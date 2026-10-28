import os
from flask import Flask, jsonify, request

app = Flask(__name__)

REGNO = os.getenv("REGNO", "unknown")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "regno": REGNO,
        "version": APP_VERSION,
        "database": False
    })


@app.route("/api/registrations", methods=["GET", "POST"])
def registrations():
    return jsonify({
        "message": "Database integration will be added in Stage 2",
        "regno": REGNO
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)