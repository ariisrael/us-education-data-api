from requests import get

def getPaginatedResults(request_url):
    r = get(request_url)
    results = r.json()["results"]
    while r.json()["next"]:
        r = get(r.json()["next"])
        results.extend(r.json()["results"])
    return results

