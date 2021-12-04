from itertools import groupby
from urllib.request import urlopen
from json import loads
import datetime

id = '192203'
url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0' \
      '%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '
data = loads(urlopen(url).read().decode('utf8'))
rev = data['query']['pages'][id]['revisions']


def convert_date(r):
    return datetime.datetime.strptime(r['timestamp'], '%Y-%m-%dT%H:%M:%SZ').date()


for key, group_items in groupby(rev, key=convert_date):
    print(key, sum(1 for i in group_items))
