import urllib.request
import os

url = 'https://sertanejoraizoficial.vercel.app/'
folder = 'c:/Users/Pichau/OneDrive/PENDRIVERS/google ads/sertanejoraiz'
os.makedirs(folder, exist_ok=True)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read()

with open(f'{folder}/index.html', 'wb') as f:
    f.write(html)
print("Done")
