from fastapi import FastAPI
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

import json

from main import app
from main import REST_COUNTRIES_REGION_ENDPOINT

import main


client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "success"}


@patch('main.get_restcountries')
def test_read_region_restcountries_404(mock_countries):
    mock_countries.return_value.status_code = 404

    response = client.get("/region/europe")

    assert response.status_code == 404
    assert response.json() == {'status_code': 404, 'detail': 'Region not found', 'headers': None}


@patch('main.get_restcountries')
def test_read_region_restcountries_403(mock_countries):
    mock_countries.return_value.status_code = 403

    response = client.get("/region/europe")

    assert response.status_code == 403
    assert response.json() == {'status_code': 403, 'detail': 'Unknown failure', 'headers': None}


@patch('main.get_restcountries')
def test_read_region_restcountries_200(mock_countries):
    f = open('/app/tests/example_countries.json', 'r')

    mock_countries.return_value.status_code = 200
    mock_countries.return_value.json.return_value = json.load(f)

    response = client.get("/region/europe")

    assert response.status_code == 200
    response_keys = list(response.json())
    response_keys.sort()
    assert response_keys == ["languages", "region"]


@patch('main.get_restcountries')
def test_read_region_restcountries_malformed(mock_countries):
    f = open('/app/tests/malformed_example_countries.json', 'r')

    mock_countries.return_value.status_code = 200
    mock_countries.return_value.json.return_value = json.load(f)

    response = client.get("/region/europe")

    assert response.status_code == 500
    assert response.json() == {'status_code': 500, 'detail': 'restcountries malformed resource', 'headers': None}
