import requests


def get_transmissions_schedule():
    try:
        # TODO - build the url programmatically
        url = "https://calendar2.priyom.org/events?timeMin=2026-04-28T00:00:00.000Z&timeMax=2026-04-29T00:00:00.000Z"
        resp = requests.get(url)
        data = resp.json()
        return data
    except requests.exceptions.RequestException as err:
        print(f"There was a problem fetching schedule: {err}")
