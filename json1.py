from itertools import groupby
from urllib.request import urlopen
from json import loads
import datetime

id = '183903'
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%93%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B8%D0%B9,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%91%D0%BE%D1%80%D0%B8%D1%81%D0%BE%D0%B2%D0%B8%D1%87'
data = loads(urlopen(url).read().decode('utf8'))
rev = data['query']['pages'][id]['revisions']


def convert_date(r):
    return datetime.datetime.strptime(r['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


for key, group_items in groupby(rev, key=convert_date):
    print(key, sum(1 for i in group_items))
