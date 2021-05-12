import requests
import logging


def main(url: str) -> str:
    logging.info("Activity started... ")
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    logging.info("Activity Completed... ")
    return response.text
