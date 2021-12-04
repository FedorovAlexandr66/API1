import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_uncos(ch: ET.Element):
    uncos = []
    for i in ch.findall('item'):
        uncos.append({
            'pubDate': i.find('pubDate').text,
            'title': i.find('title').text
        })
    return uncos


def get_top_limb():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def keep_json(ch):
    json_file = json.dumps(get_uncos(ch), ensure_ascii=False).encode('utf8')
    with open("news.json", 'wb') as f:
        f.write(json_file)


channel = get_top_limb()
keep_json(channel)