import requests

def get_version() -> str:
    try:
        r = requests.get("https://flyff-api.sniegu.fr/version/data")
        return r.text
    except:
        print("Failed to get version")
        raise
