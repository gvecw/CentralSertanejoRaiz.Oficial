import urllib.request
import urllib.parse
import os
import re

url = 'https://sertanejoraizoficial.vercel.app/'
folder = 'c:/Users/Pichau/OneDrive/PENDRIVERS/google ads/sertanejoraiz'
os.makedirs(folder, exist_ok=True)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

# Find all relative links
assets = set()
for m in re.finditer(r'(?:src|href)="([^"]+)"', html):
    link = m.group(1)
    if not link.startswith('http') and not link.startswith('data:') and not link.startswith('#'):
        assets.add(link)

for asset in assets:
    asset_url = urllib.parse.urljoin(url, urllib.parse.quote(asset))
    asset_path = os.path.join(folder, urllib.parse.unquote(asset))
    try:
        req_asset = urllib.request.Request(asset_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req_asset) as response:
            asset_data = response.read()
        
        os.makedirs(os.path.dirname(asset_path), exist_ok=True)
        with open(asset_path, 'wb') as f:
            f.write(asset_data)
        print(f"Downloaded {asset}")
    except Exception as e:
        print(f"Failed to download {asset}: {e}")

# Remove tracking scripts
html = re.sub(r'<script>\s*window\.pixelId.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script src="https://cdn\.utmify\.com\.br/scripts/utms/latest\.js".*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script type="text/javascript">\s*\(function\(c,l,a,r,i,t,y\).*?</script>', '', html, flags=re.DOTALL)

with open(f'{folder}/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
