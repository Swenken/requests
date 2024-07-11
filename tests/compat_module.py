import pytest
from requests.compat import StringIO
from urllib.parse import urljoin

def test_stringio_import():
    assert StringIO is not None

def test_stringio_import_error(monkeypatch):
    monkeypatch.delattr("requests.compat", "StringIO")
    import io as StringIO
    assert StringIO is not None

def test_urljoin_python2(monkeypatch):
    # Simulate Python 2 environment by monkeypatching urljoin
    monkeypatch.setattr("urllib.parse.urljoin", lambda base, url: base + url)
    assert urljoin("http://example.com", "/test") == "http://example.com/test"

def test_urljoin_python3():
    # Test urljoin in Python 3
    assert urljoin("http://example.com", "/test") == "http://example.com/test"
