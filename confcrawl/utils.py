from pathlib import Path
from time import sleep
from urllib import parse

import requests
from lxml import html

root_dir = Path(__file__).parents[1]


def _get_snippet(root: html.HtmlElement, keyword: str):
    """Retrieve snippet result

    Args:
        root: searched result html
        keyword: query
    """
    snippet_link = root.xpath(
        "//*[@id='rso']/div[1]/div[1]/div/div[1]/div/div/div/div[1]/a/@href"
    )
    snippet_title = root.xpath(
        "//*[@id='rso']/div[1]/div[1]/div/div[1]/div/div[2]/div/div[1]/a/h3/span/text()"
    )
    if (
        len(snippet_link) > 0
        and "arxiv" in snippet_link[0]
        and keyword[:20] == snippet_title[0][:20]
    ):  # google collapses long title
        return snippet_link[0]
    else:
        return None


def _get_top_retrieval(root: html.HtmlElement, keyword: str):
    """Retrieve matched document in top 1-2 search results

    Args:
        root: searched result html
        keyword: query
    """
    retrevied_doc_hrefs = root.xpath("//*[@id='rso']/div/div/div[1]/a/@href")
    retrevied_doc_titles = root.xpath("//*[@id='rso']/div/div/div[1]/a/h3/span/text()")
    if len(retrevied_doc_hrefs) == 0:
        return None
    for href, title in zip(
        retrevied_doc_hrefs[:1], retrevied_doc_titles[:1]
    ):  # considered github
        if "arxiv" in href and keyword[:20] == title[:20]:
            return href
    else:
        return None


def search_google(keyword: str, sleep_time: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Content-Type": "text/plain;charset=UTF-8",
    }
    base_url = "https://www.google.com/search?q={}"

    url_parsed_keyword = parse.quote(keyword.replace(" ", "-"))
    url = base_url.format(url_parsed_keyword)

    sleep(sleep_time)
    r = requests.get(url, headers=headers)
    root = html.fromstring(r.text)
    if r.ok:
        arxiv = _get_snippet(root, keyword)
        if arxiv is None:
            arxiv = _get_top_retrieval(root, keyword)
            if arxiv is None:
                arxiv = "N/A"
        return arxiv
    else:
        return "N/A"
