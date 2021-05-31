import requests
import json
import os

os.system("clear")


def get_track_uris(token):
    auth_headers = {"Authorization" : "Bearer " + token}
    offset = ["0", "50", "100"]
    uris = []

    for i in offset:
        request_url = "https://api.spotify.com/v1/me/tracks?market=US&limit=50&offset=" + i

        response = requests.get(
            request_url,
            headers=auth_headers
        )

        json_dict = response.json()

        for i, val in enumerate(json_dict["items"]):
            uris.append(json_dict["items"][i]["track"]["uri"])

    return uris[:126]


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def add_to_playlist(token):
    auth_headers = {"Authorization" : "Bearer " + token}
    playlist_id = ""
    tracks_array = get_track_uris(token)[:100]
    payload = json.dumps({"uris": tracks_array})
    request_url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"

    response = requests.post(
        request_url,
        headers=auth_headers,
        data=payload
    )

    print(response.text)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

token = ""
add_to_playlist(token)