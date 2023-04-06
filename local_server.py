from flask import Flask
from flask import redirect, request
import requests
from itsdangerous import base64_encode
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

url = os.getenv("LOCAL_URL")
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

@app.route("/spotify/login", methods=["GET"])
def spotifyLogin():
    return redirect(f"https://accounts.spotify.com/authorize?scope=user-read-private user-read-email user-read-playback-state playlist-read-private&client_id={client_id}&response_type=code&redirect_uri={url}/spotify/callback")

@app.route("/spotify/callback", methods=["GET"])
def spotifyCallback():
    code = request.args["code"]
    headers = {
        "Authorization": "Basic " + base64_encode(f"{client_id}:{client_secret}").decode(),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    r = requests.post(
        "https://accounts.spotify.com/api/token", data={
            "grant_type": "authorization_code",
            "redirect_uri": f"{url}/spotify/callback",
            "code": code
        }, headers=headers)
    

    access_token = r.json()["access_token"]
    refresh_token = r.json()["refresh_token"]
    
    print("Access Token")
    print(access_token)
    print("Refresh Token")
    print(refresh_token)

    return

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3412)

