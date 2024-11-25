import pytest
from fastapi.testclient import TestClient

from fast_one.app import app


@pytest.fixture
def client():
    return TestClient(app)
