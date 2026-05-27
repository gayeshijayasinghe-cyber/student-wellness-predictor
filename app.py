"""Simple Flask application for student wellness predictor."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    """Home route."""
    return "Smart Student Wellness Predictor Running"


@app.route('/health')
def health():
    """Health check route."""
    return "Application Healthy"


if __name__ == '__main__':
    app.run(port=5000)
