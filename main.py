import requests
import os
import json
import sys
import base64

insta_id = ""
img = open("img.jpg", "rb")
curl = f"https://api.imgbb.com/1/upload?key={IMGKEY}"
r = requests.post(curl, files={"image": img})
image_url = r.json()["data"]["url"]
print(image_url)

url = f"https://graph.facebook.com/v16.0/{insta_id}/media?image_url={image_url}&caption=bot&access_token={os.environ['ins_token']}"
r = requests.post(url)
json_d = json.loads(r.text)
print(json_d)
img_id = json_d["id"]
url = f"https://graph.facebook.com/v16.0/{insta_id}/media_publish?creation_id={img_id}&access_token={os.environ['ins_token']}"
print(url)
r = requests.post(url)
print(r.text)
