from fastapi import FastAPI, Response, HTTPException

import requests
import util


REST_COUNTRIES_REGION_ENDPOINT = "https://restcountries.eu/rest/v2/region"
app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "success"}


@app.get("/region/{region}")
def read_region(region: str, response: Response):
    r = get_restcountries(region)

    if r.status_code == 404:
        # FastAPI appears to have a bug, have to manually set status code
        response.status_code = 404
        return HTTPException(status_code=404, detail="Region not found")

    # Handle all other unknown errors
    if r.status_code != 200:
        # FastAPI appears to have a bug, have to manually set status code
        response.status_code = r.status_code
        return HTTPException(status_code=r.status_code, detail="Unknown failure")

    try:
        unique_languages = util.unique_languages(r.json())
    except KeyError:
        # FastAPI appears to have a bug, have to manually set status code
        response.status_code = 500
        return HTTPException(status_code=500, detail="restcountries malformed resource")

    return {"region": region, "languages": unique_languages}


def get_restcountries(region):
    return requests.get(f"{REST_COUNTRIES_REGION_ENDPOINT}/{region}")
