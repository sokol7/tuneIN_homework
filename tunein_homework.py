import requests
import json


def merge_response(url):
    # Call the target api endpoint and receive it's content in json format
    r = requests.get(url)
    if r.status_code != 200:
        return False
    res = json.loads(r.text)

    # Construct a new dict where  key: priority value / value: dict with values
    new_res = {}
    for i in res["ranked"]:
        new_res[i["priority"]] = i["vals"]

    # Sort the constructed dict by the priority in descending order
    sorted_res = dict(sorted(new_res.items(), reverse=True))

    # Merge values according to their priority, where lower priority overwrites higher priority
    result = {}
    for i in sorted_res.values():
        for j in i:
            if not j.startswith('skip'):
                result[j] = i[j]
    return result
