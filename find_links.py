import re

with open('sertanejoraiz/index.html', encoding='utf-8') as f:
    html = f.read()

# find all anchor tags
matches = re.finditer(r'<a([^>]+)>', html, re.IGNORECASE)
for m in matches:
    attrs = m.group(1)
    if 'href' in attrs:
        print(attrs)
