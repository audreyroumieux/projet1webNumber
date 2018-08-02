import printerApi.settings
import requests
from requests.auth import HTTPBasicAuth

api_uri = "http://127.0.0.1:8000/"
data = {"name" : "Ninja", "points":1000}
files = {"image": open(printerApi.settings.MEDIA_ROOT + '/images/objects/cbb8533e68df9ba15b645071a819aef8_preview_featured.jpg', 'rb')}
r = requests.post(api_uri + "objects/", files=files, data=data,
                  auth=HTTPBasicAuth('admin', 'password123'))
print(r.text)