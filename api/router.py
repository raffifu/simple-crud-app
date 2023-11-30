import requests
from logging import Logger
from fastapi import APIRouter, status
from api.helpers import api_response, save_to_file

router = APIRouter()
logger = Logger("router")

DUMMY_CSV = "https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv"


@router.post("/generate")
def generate():
    """Download CSV file and save to output folder."""
    try:
        response = requests.get(DUMMY_CSV)
        response.raise_for_status()

        filename = "output/dummy.csv"
        save_to_file(filename, response.text)

        return api_response(
            status.HTTP_200_OK,
            "Successfully Downloaded",
            {
                "filename": filename,
            },
        )
    except Exception as err:
        logger.error(err)

        return api_response(
            status.HTTP_500_INTERNAL_SERVER_ERROR, "Internal Server Error."
        )
