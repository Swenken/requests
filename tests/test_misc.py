import pytest
import ssl
from urllib.parse import urljoin
from requests.compat import urljoin

def test_urljoin_edge_cases():
    assert urljoin("http://example.com", "") == "http://example.com"
    assert urljoin("http://example.com", "/") == "http://example.com/"
    assert urljoin("http://example.com/path/", "/newpath") == "http://example.com/newpath"
    assert urljoin("http://example.com/path", "newpath") == "http://example.com/newpath"

@pytest.fixture
def mock_ssl_context():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    yield context

def test_ssl_context(mock_ssl_context):
    assert isinstance(mock_ssl_context, ssl.SSLContext)
    assert mock_ssl_context.verify_mode == ssl.CERT_REQUIRED

def test_prepare_url_special_characters(prepare_url):
    class MockResponse:
        url = "http://example.com/path"

    result = prepare_url(MockResponse())
    assert result("subpath?query=1&another=2") == "http://example.com/path/subpath?query=1&another=2"

def test_nosan_server_with_different_ca(tmp_path_factory, monkeypatch, nosan_server):
    class MockCA:
        def __init__(self):
            self.cert_pem = MockCertPem()

        def issue_cert(self, common_name):
            return MockCert()

    class MockCertPem:
        def write_to_path(self, path):
            with open(path, "w") as f:
                f.write("Different Mock CA certificate")

    class MockCert:
        def configure_cert(self, context):
            pass

    monkeypatch.setattr("trustme.CA", MockCA)
    result = nosan_server(tmp_path_factory)
    assert result[0] == "localhost"
    assert isinstance(result[1], int)
    assert result[2].endswith("ca.pem")

def test_prepare_url_with_fragment(prepare_url):
    class MockResponse:
        url = "http://example.com/path"

    result = prepare_url(MockResponse())
    assert result("subpath#section") == "http://example.com/path/subpath#section"

def test_ssl_context_with_different_cipher(monkeypatch):
    def mock_create_default_context(purpose):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256')
        return context

    monkeypatch.setattr(ssl, 'create_default_context', mock_create_default_context)

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    assert 'ECDHE-RSA-AES128-GCM-SHA256' in context.get_ciphers()[0]['name']
