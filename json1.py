import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json


def get_top_limb():
    data = urlopen('https://lenta.ru/rss').read().decode('utf8')
    root = ET.fromstring(data)
    return root[0]


def get_uncos(ch: ET.Element):
    uncos = []
    for i in ch.findall('item'):
        uncos.append({
            'pubDate': i.find('pubDate').text,
            'title': i.find('title').text
        })
    return uncos


def get_full_uncos(ch: ET.Element):
    full_uncos = []
    for i in ch.findall('item'):
        fields_dict = {}
        for f in i:
            fields_dict[f.tag] = f.text
        full_uncos.append(fields_dict)
    return full_uncos


def keep_json(file_name, uncos):
    json_file = json.dumps(uncos, ensure_ascii=False).encode('utf8')
    with open(file_name, 'wb') as f:
        f.write(json_file)


channel = get_top_limb()
keep_json("full_uncos.json", get_full_uncos(channel))