from django.shortcuts import render
from django.http import HttpResponse
import requests
from xml_parse.models import Items, MediaType, Headers, Stories
from bs4 import BeautifulSoup
from datetime import datetime
from django.utils import timezone


def mediat(mtype):
    obj, _ = MediaType.objects.get_or_create(mtype=mtype)
    return obj


def dtcteate(date, time):
    my_datetime = datetime.strptime(date + time, "%Y%m%d%H:%M",)
    return timezone.make_aware(my_datetime, timezone.get_current_timezone())


def parag(r):
    nm = []
    for i in r:
        if i.text == '':
            nm.append('\n')
        else:
            nm.append(i.text)
    return ''.join(nm)


def header(inp):
    author = inp.find('author').string
    media = inp.find('media').string
    country = inp.find('country').string
    name = inp.find('name').string
    product = inp.find('product').string
    term = inp.find('term').string
    mediatype = mediat(inp.find('media')['type'])
    datetime = dtcteate(inp.find('date').string, inp.find('hour').string)
    head = Headers(
        author=author,
        media=media,
        country=country,
        name=name,
        product=product,
        term=term,
        mediatype=mediatype,
        datetime=datetime, )
    head.save()
    # return header.id
    return head


def story(inp):
    lang = inp['lang']
    keywords = inp.find('keywords').string
    title = inp.find('title').string
    summary = inp.find('summary').string
    paragraph = parag(inp.find_all("paragraph"))
    stor = Stories(
        lang=lang,
        keywords=keywords,
        title=title,
        summary=summary,
        paragraph=paragraph)
    stor.save()
    # return story.id
    return stor


def init(request):
    url = 'https://feed.tradingcentral.com/ws_ta.asmx/GetFeed'
    PARAMS = {'type_product': 'null',
              'product': 'null',
              'term': 'null',
              'days': 1,
              'last_ta': False,
              'culture': 'en-US',
              # or ar-AE    # TODO: move to settings
              'partner': 854,
              'token': 'VGq4xJzr9+0Y68LcKJFiig=='}
    # res = requests.get(url,params=PARAMS)

    with open('qw.xml', "r") as f:
        res = f.read()

    inp = BeautifulSoup(res, features='xml')

    for art in inp('article'):
        aid = art["id"]
        astatus = art["status"]
        atype = art.find("analysis")["type"]
        header_id = header(art.find("header"))
        story_id = story(art.find("story"))
        item = Items(id=aid, status=astatus, analysis=atype, header=header_id, story=story_id)
        item, created = Items.objects.get_or_create(id=aid)
        item.save()
    return HttpResponse("OK")