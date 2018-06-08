from PIL import Image
import requests
from io import BytesIO

url = 'http://imgur.com/HzafyBA.jpg'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()

predict_from_url("http://imgur.com/HzafyBA.jpg")

ox - predict_from_url("http://imgur.com/HzafyBA.jpg")