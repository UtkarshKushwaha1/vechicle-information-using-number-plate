# from unittest import result
import requests
from pprint import pprint
import xmltodict
import json
regions = ['mx', 'us-ca', 'in']  # Change to your country
with open('car.jfif', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token bab16cc6d38270a52881630b11aabffe4ccb2ca4'})
res = response.json()
pprint(res)

response = requests.get(
    f"http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={res['results'][0]['plate']}&username={'boldfinal'} ")

v = (xmltodict.parse(response.content))

info = v['Vehicle']['vehicleJson']

ans = json.loads(info)

print(ans["Description"])

from PIL import Image, ImageDraw

img = Image.open('car.jfif')
d1 = ImageDraw.Draw(img)
d1.text((12, 12),"Description:"+ans["Description"]+"\n", fill=(255, 0, 0)) 
d1.text((44, 44),"RegistrationYear: "+ans["RegistrationYear"], fill=(255, 0, 0))
d1.text((88, 88),"Location: "+ans["Location"], fill=(255, 0, 0))
d1.text((120,120),"RegistrationDate: "+ans["RegistrationDate"], fill=(255, 0, 0))
img.show()
img.save("sol.jfif")



