"""Tests for Flask application."""

from app import app


def test_home():
    """Test home route."""
    tester = app.test_client()
    response = tester.get('/')

    if response.status_code != 200:
        raise Exception("Status code is not 200")