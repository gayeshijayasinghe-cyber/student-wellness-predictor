"""Student Wellness Predictor Flask application."""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Home endpoint."""
    return "Student Wellness Predictor Running"


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # nosec B104
