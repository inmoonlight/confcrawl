from pathlib import Path

import requests
from lxml import html
from urllib import parse
from time import sleep

root_dir = Path(__file__).parents[1]


def _get_snippet(root):
    # snippet = root.xpath("/html/body/div[7]/div[2]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div/div[1]/a/@href")
    snippet = root.xpath("//*[@id='rso']/div[1]/div[1]/div/div[1]/div/div/div/div[1]/a/@href")
    if len(snippet) > 0 and "arxiv" in snippet[0]:
        return snippet[0]
    else:
        return None


def _get_top_retrieval(root):
    retrevied_doc = root.xpath("//*[@id='rso']/div/div/div[1]/a/@href")
    if len(retrevied_doc) == 0:
        return None
    for doc in retrevied_doc[:1]:  # considered github
        if "arxiv" in doc:
            return doc
    else:
        return None


def search_google(keyword: str, sleep_time: int):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'Content-Type': 'text/plain;charset=UTF-8'
    }
    base_url = "https://www.google.com/search?q={}"

    keyword = keyword.replace(" ", '-')
    keyword = parse.quote(keyword)
    url = base_url.format(keyword)

    sleep(sleep_time)
    r = requests.get(url, headers=headers)
    root = html.fromstring(r.text)
    if r.ok:
        arxiv = _get_snippet(root)
        if arxiv is None:
            arxiv = _get_top_retrieval(root)
            if arxiv is None:
                arxiv = "N/A"
        return arxiv
    else:
        return "N/A"
